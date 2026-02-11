from flask import flash, render_template
from typing import Dict, Union, Literal, Optional, Callable
import math
from App.model.logger import logger

# =================== Processar Mensagem ===================
def processar_mensagem(
    template: Optional[str] = None,
    contexto: Optional[Dict] = None,
    mensagem: str = "",
    nivel: Literal["INFO", "WARNING", "ERROR", "CRITICAL", "DEBUG"] = "ERROR",
    tipo_flash: Literal["success", "info", "warning", "danger"] = "danger",
    contexto_extra: Optional[Dict] = None
):
    contexto = contexto or {}
    contexto_extra = contexto_extra or {}

    nivel = nivel.upper()
    if nivel not in ["INFO", "WARNING", "ERROR", "CRITICAL", "DEBUG"]:
        nivel = "ERROR"

    getattr(logger, nivel.lower())("%s", mensagem)
    flash(mensagem, tipo_flash)

    if template:
        return render_template(template, **contexto, **contexto_extra)
    return None

# =================== Renderizar Com Mensagem ===================
def renderizar_com_mensagem(template: str, contexto: dict, mensagem: str, nivel: str, tipo_flash: str): 
    processar_mensagem(template=template, contexto=contexto, mensagem=mensagem, nivel=nivel, tipo_flash=tipo_flash)
    return render_template(template, **contexto)

# =================== Processar Resultado ===================
def processar_resultado(
    result: Union[Dict, bool],
    success_message: str,
    error_message: str = "Erro na operação",
    extra_context: Optional[Dict] = None
) -> bool:
    extra_context = extra_context or {}

    if isinstance(result, bool):
        result = {"success": result, "message": success_message if result else error_message}

    sucesso = result.get("success", False)
    mensagem = result.get("message", success_message if sucesso else error_message)

    nivel_log = "INFO" if sucesso else "WARNING"
    tipo_flash = "success" if sucesso else "warning"

    processar_mensagem(mensagem=mensagem, nivel=nivel_log, tipo_flash=tipo_flash, contexto_extra=extra_context)
    
    return sucesso

# =================== Função de Validação de Campos ===================
def processar_validacao(
    campos: dict[str, str], 
    tipo: str = "obrigatorio", 
    validacoes_adicionais: Optional[dict[str, Callable]] = None
) -> bool:
    erros = []

    if tipo == "obrigatorio":
        for campo, valor in campos.items():
            if not valor.strip():
                erros.append(f"O campo '{campo}' é obrigatório.")

    if validacoes_adicionais:
        for campo, validacao in validacoes_adicionais.items():
            if campo in campos:
                try:
                    resultado = validacao(campos[campo])
                    if resultado is not True:
                        erros.append(f"Erro no campo '{campo}': {resultado}")
                except Exception as e:
                    erros.append(f"Erro ao validar o campo '{campo}': {str(e)}")

    if erros:
        processar_mensagem(mensagem="\n".join(erros), nivel="ERROR", tipo_flash="danger")
        return False

    return True

# =================== Funções de Paginação ===================
def processar_paginacao(lista, page, per_page, sort_key=None, reverse=False):
    try:
        page = max(1, int(page))
    except ValueError:
        page = 1

    if sort_key:
        lista = sorted(lista, key=sort_key, reverse=reverse)

    total_items = len(lista)
    total_pages = max(1, math.ceil(total_items / per_page) if per_page > 0 else 1)

    if page > total_pages:
        mensagem = "Não há resultados para exibir." if total_items == 0 else "Página fora do alcance."
        processar_mensagem(mensagem=mensagem, nivel="INFO", tipo_flash="warning", contexto_extra={"page": page})
        return [], total_items, total_pages, page, False, total_pages > 1

    start, end = (page - 1) * per_page, page * per_page
    paginacao = lista[start:end]

    return paginacao, total_items, total_pages, page, page < total_pages, page > 1

# =================== Mensagens Centralizadas ===================

MESSAGENS = {
    "sessao_expirada": (
        "Sua sessão expirou! Por motivos de segurança, você precisará fazer login.",
        "warning", "warning"
    ),
    "logout_sucesso": (
        "Você foi desconectado com sucesso! Esperamos vê-lo novamente em breve.", "info", "info"
    ),
    "credenciais_incorretas": (
        "Credenciais inválidas! O nome de usuário ou a senha informados estão incorretos.",
        "danger", "warning"
    ),
    "autenticacao_efetuada": (
        "Bem-vindo(a), {email}! Seu nível de acesso é {nivel_acesso}.", "success", "info"
    ),
    "acesso_negado": (
        "Acesso negado! Você não tem permissão para acessar este recurso.", "danger", "warning"
    ),
}

# -------------------------- Funções de Mensagens --------------------------

def get_mensagem(chave, **kwargs):
    mensagem, tipo_flash, nivel = MESSAGENS.get(chave, ("Mensagem não definida.", "info", "info"))
    mensagem_formatada = mensagem.format(**kwargs)
    return {
        "mensagem": mensagem_formatada,
        "tipo_flash": tipo_flash,
        "nivel": nivel
    }








