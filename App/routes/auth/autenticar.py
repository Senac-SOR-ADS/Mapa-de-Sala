from flask import redirect, url_for
from functools import wraps
from App.controllerWeb.login import validarLogin, pegarUsuarioLogado
from App.routes.auth.acesso import validar_acesso, verificar_sessao, registrar_acesso
from App.routes.utils import processar_mensagem, get_mensagem

# ------------------------------------------------------------------------------
# Autentica o usuário verificando suas credenciais e registra o acesso
# ------------------------------------------------------------------------------

def autenticar(username, password):
    if not validarLogin(username, password):
        processar_mensagem(**get_mensagem("credenciais_incorretas"))
        return False
    usuario = pegarUsuarioLogado()
    if usuario and usuario.get('email'):
        nivel_acesso = usuario.get('nivel_acesso')
        registrar_acesso()
        processar_mensagem(**get_mensagem("autenticacao_efetuada", email=usuario['email'], nivel_acesso=nivel_acesso))
        return True
    processar_mensagem(**get_mensagem("credenciais_incorretas"))
    return False

# ------------------------------------------------------------------------------
# Verifica se o usuário está autenticado, se a sessão é válida e se possui o nível de acesso necessário
# ------------------------------------------------------------------------------

def verificar_autenticacao(nivel_requerido=None):   
    if not verificar_sessao():
        processar_mensagem(**get_mensagem("sessao_expirada"))
        return redirect(url_for('login_route.login'))
    if nivel_requerido:
        if isinstance(nivel_requerido, list):
            if not any(validar_acesso(nivel_requerido=nivel) for nivel in nivel_requerido):
                processar_mensagem(**get_mensagem("acesso_negado"))
                return redirect(url_for('login_route.login'))
        elif not validar_acesso(nivel_requerido=nivel_requerido):
            processar_mensagem(**get_mensagem("acesso_negado"))
            return redirect(url_for('login_route.login'))
    return True

# ------------------------------------------------------------------------------
# Decorador para verificar autenticação e nível de acesso antes de executar a função
# ------------------------------------------------------------------------------

def autenticacao_requerida(nivel=None):   
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            autenticado = verificar_autenticacao(nivel_requerido=nivel)
            if autenticado is not True:
                return autenticado
            return f(*args, **kwargs)
        return decorated_function
    return decorator

login_auth = autenticacao_requerida()
admin_auth = autenticacao_requerida(nivel=['admin'])
admin_suporte_auth = autenticacao_requerida(nivel=['admin', 'suporte'])
