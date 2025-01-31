from flask import session
from App.controller.login import pegarUsuarioLogado, removerUsuarioLogado
from datetime import datetime
from App.routes.logger_setup import logger
from App.routes.auth.config import Config

# =================== Verificação de Expiração ===================
def verificar_expiracao():
    """Verifica se a sessão expirou com base na configuração."""
    if session.get('usuario') and session.permanent:
        expiration_time = session.get('last_activity_time')
        if expiration_time:
            expiration_time = expiration_time.replace(tzinfo=None)
            session_lifetime = Config.PERMANENT_SESSION_LIFETIME
            if datetime.now() > expiration_time + session_lifetime:
                session.clear()
                logger.info("Sessão expirada e removida.")
                return False
        session['last_activity_time'] = datetime.now()
        session.modified = True
    return True

# =================== Validação de Acesso ===================
def validar_acesso(nivel_requerido=None):
    """Verifica se o usuário está autenticado e possui o nível de acesso necessário."""
    try:
        usuario, nivel_acesso = pegar_acesso()
        if not usuario or not nivel_acesso:
            return False
        if nivel_requerido and nivel_acesso != nivel_requerido:
            logger.warning(f"Tentativa de acesso não autorizado. Usuário ID: {usuario.get('id_login')}.")
            return False
        return True
    except Exception as e:
        logger.error(f"Erro ao validar acesso: {str(e)}", exc_info=True)
        return False

# =================== Registro de Acesso ===================
def registrar_acesso():
    """Registra o usuário na sessão e sincroniza com o estado logado."""
    try:
        if not verificar_expiracao():
            return
        usuario = pegarUsuarioLogado()
        if usuario and usuario.get('email') and usuario.get('id_login'):
            session.update({
                'usuario': usuario,
                'nivel_acesso': usuario.get('nivel_acesso'),
                'permanent': True,
                'last_activity_time': datetime.now(),
            })
            session.permanent_session_lifetime = Config.PERMANENT_SESSION_LIFETIME
            logger.info(f"Usuário registrado: ID {usuario['id_login']}, Email {usuario['email']}, Nível {usuario['nivel_acesso']}.")
        else:
            session.clear()
            logger.warning("Falha ao registrar usuário: informações incompletas.")
    except Exception as e:
        logger.error(f"Erro ao registrar acesso: {str(e)}", exc_info=True)

# =================== Remoção de Acesso ===================
def remover_acesso():
    """Remove o estado logado e limpa a sessão."""
    try:
        if not verificar_expiracao():
            return
        removerUsuarioLogado()
        usuario = session.pop('usuario', None)
        if usuario:
            logger.info(f"Usuário deslogado: ID {usuario['id_login']}, Email {usuario['email']}, Nível {usuario['nivel_acesso']}.")
        session.clear()
    except Exception as e:
        logger.error(f"Erro ao remover acesso: {str(e)}", exc_info=True)

# =================== Pegar Informações de Acesso ===================
def pegar_acesso():
    """Retorna as informações do usuário logado e o nível de acesso."""
    try:
        usuario = session.get('usuario')
        nivel_acesso = session.get('nivel_acesso')
        if not usuario or not usuario.get('email') or not usuario.get('id_login'):
            session.clear()
            return None, None
        return usuario, nivel_acesso
    except Exception as e:
        logger.error(f"Erro ao buscar informações de acesso: {str(e)}", exc_info=True)
        return None, None
