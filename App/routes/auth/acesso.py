from flask import session
from time import time
from datetime import datetime
from App.routes.utils import processar_mensagem, get_mensagem
from App.controllerWeb.login import pegarUsuarioLogado, removerUsuarioLogado, pegar_acesso
from App.routes.auth.config import Config
from threading import Lock
from App.model.logger import logger

# ------------------------------------------------------------------------------
# =================== Flags de Controle ===================
# ------------------------------------------------------------------------------

SESSION_FLAGS = {"acesso_em_progresso": False, "expiracao_em_progresso": False}
lock_sessao = Lock()

# =================== Funções de Sessão ===================

# ------------------------------------------------------------------------------
# Verifica o estado da sessão: se a sessão foi encerrada, expirou ou está ativa
# ------------------------------------------------------------------------------

def verificar_sessao(expirar: bool = None) -> bool:
    try:
        with lock_sessao:
            if expirar is not None:
                session.pop('logout_realizado', None)
                session.pop('sessao_expirada', None)
                session['sessao_expirada' if expirar else 'logout_realizado'] = True
                return False

            if session.pop('logout_realizado', False) or session.pop('sessao_expirada', False):
                session['sessao_expirada'] = True
                return False

            return bool(session.get('usuario')) and session.permanent
        
    except Exception as e:
        logger.error("Erro ao verificar sessão: %s", str(e))
        return False

# ------------------------------------------------------------------------------
# Remove o acesso do usuário
# ------------------------------------------------------------------------------

def remover_acesso(expirar: bool = False) -> bool:
    try:
        verificar_sessao(expirar)
        removerUsuarioLogado()
        limpar_sessao(expirar)
        mensagem = get_mensagem("sessao_expirada" if expirar else "logout_sucesso")
        processar_mensagem(**mensagem)
        return True

    except Exception as e:
        logger.error("Erro ao remover acesso: %s", str(e))
        return False

# ------------------------------------------------------------------------------
# Limpa a sessão do usuário
# ------------------------------------------------------------------------------

def limpar_sessao(expirar: bool):
    for key in ['usuario', 'nivel_acesso', 'last_activity_time']:
        session.pop(key, None)
    verificar_sessao(expirar)

# ------------------------------------------------------------------------------
# Atualiza o tempo da sessão
# ------------------------------------------------------------------------------

INTERVALO_MINIMO_EXPIRACAO = 120
def atualizar_tempo_sessao():
    if verificar_sessao():
        ultima_expiracao = session.get('ultima_expiracao', 0)
        agora = time()
        if agora - ultima_expiracao >= INTERVALO_MINIMO_EXPIRACAO:
            with lock_sessao:
                if session.get('ultima_expiracao', 0) == ultima_expiracao:
                    session['last_activity_time'] = datetime.now().isoformat()
                    session['ultima_expiracao'] = agora

# -------------------------- Funções de Acesso e Processos ---------------------

# ------------------------------------------------------------------------------
# Registra o acesso do usuário
# ------------------------------------------------------------------------------

def registrar_acesso():
    usuario = pegarUsuarioLogado()
    if not usuario:
        logger.warning("Tentativa de acesso com usuário não encontrado")
        return

    session.clear()
    session.permanent = True
    session.update({
        'usuario': usuario,
        'nivel_acesso': usuario.get('nivel_acesso'),
        'last_activity_time': datetime.now().isoformat(),
    })
    session.pop('sessao_expirada', None)
    atualizar_tempo_sessao()

# ------------------------------------------------------------------------------
# Controla processos na sessão (iniciar ou finalizar)
# ------------------------------------------------------------------------------

def controlar_processo(processo: str, acao: str) -> bool:
    if acao not in {"iniciar", "finalizar"}:
        return False
    try:
        if acao == "iniciar":
            if not session.get(processo, False):
                session[processo] = True
            return True
        elif acao == "finalizar":
            session.pop(processo, None)
            return True
    except Exception as e:
        logger.error("Erro ao controlar o processo '%s': %s", processo, str(e))
        return False

# ------------------------------------------------------------------------------
# Valida o acesso do usuário (incluindo nível de acesso)
# ------------------------------------------------------------------------------

def validar_acesso(nivel_requerido=None) -> bool:
    try:
        usuario, nivel_acesso = pegar_acesso()
        if not usuario or not nivel_acesso:
            logger.warning("Falha na validação de acesso: usuário ou nível de acesso não encontrados")
            return False
        if not (controlar_processo("acesso_em_progresso", "iniciar") and verificar_sessao()):
            return False
        atualizar_tempo_sessao()
        if nivel_requerido:
            niveis_permitidos = [str(n).strip().lower() for n in (nivel_requerido if isinstance(nivel_requerido, list) else [nivel_requerido])]
            if str(nivel_acesso).strip().lower() not in niveis_permitidos:
                logger.warning("Acesso negado: nível de acesso insuficiente")
                return False
        return True
    except Exception as e:
        logger.error("Erro ao validar acesso: %s", str(e))
        return False

# -------------------------- Funções de Expiração de Sessão --------------------------

# ------------------------------------------------------------------------------
# Verifica se a sessão expirou
# ------------------------------------------------------------------------------

def sessao_expirada() -> bool:
    with lock_sessao:
        if SESSION_FLAGS["expiracao_em_progresso"]:
            return True
        SESSION_FLAGS["expiracao_em_progresso"] = True

    expiration_time = session.get('last_activity_time')
    if not expiration_time:
        limpar_sessao(expirar=True)
        return True
    try:
        delta = datetime.now() - datetime.fromisoformat(expiration_time)
    except ValueError as e:
        if "invalid isoformat string" in str(e).lower():
            limpar_sessao(expirar=True)
            logger.warning("Formato inválido de data ao verificar expiração de sessão")
        else:
            limpar_sessao(expirar=True)
        return True
    if delta > Config.PERMANENT_SESSION_LIFETIME:
        limpar_sessao(expirar=True)
        return True
    with lock_sessao:
        SESSION_FLAGS["expiracao_em_progresso"] = False
    return False

# ------------------------------------------------------------------------------
# Verifica se a sessão expirou e toma ações apropriadas
# ------------------------------------------------------------------------------

def verificar_expiracao(remover=False) -> bool:
    if 'usuario' not in session:
        return False
    if session.get('validando_expiracao', False):
        return False
    session['validando_expiracao'] = True
    try:
        session.setdefault('ultima_expiracao', time())
        agora = time()
        ultima_expiracao = session['ultima_expiracao']
        if agora - ultima_expiracao < INTERVALO_MINIMO_EXPIRACAO:
            return False
        session['ultima_expiracao'] = agora
        if not controlar_processo("expiracao_em_progresso", "iniciar"):
            return False
        expirou = 'logout_realizado' not in session and (not verificar_sessao() or sessao_expirada())
        if expirou:
            if remover:
                remover_acesso(expirar=True)
            return False
        atualizar_tempo_sessao()
        return True
    finally:
        session['validando_expiracao'] = False
