from flask import redirect, url_for, flash, session
from App.controller.login import validarLogin
from App.routes.auth.acesso import validar_acesso, registrar_acesso
from functools import wraps

def autenticar(username, password):
    """Autentica um usuário verificando suas credenciais."""
    try:
        if validarLogin(username, password):
            registrar_acesso()
            return True
    except Exception:
        pass
    return False

# Decorator para verificar se o usuário está autenticado
def login_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not validar_acesso():
            flash("Você precisa estar logado para acessar esta página.", 'warning')
            return redirect(url_for('login_route.login'))
        return f(*args, **kwargs)
    return decorated_function

