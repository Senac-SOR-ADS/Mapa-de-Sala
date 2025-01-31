from flask import redirect, url_for, flash
from functools import wraps
from App.controller.login import validarLogin, pegarUsuarioLogado
from App.routes.auth.acesso import validar_acesso, registrar_acesso

# =================== Autenticação ===================
def autenticar(username, password):
    """Autentica um usuário verificando suas credenciais e registra o acesso."""
    try:
        if validarLogin(username, password):
            usuario = pegarUsuarioLogado()
            if usuario and usuario.get('email') and usuario.get('id_login'):
                registrar_acesso()
                flash(f"Usuário {usuario['email']} autenticado com sucesso.", "info")
                return True
            flash("Erro ao registrar usuário após autenticação. Dados inválidos.", "danger")
            return False
        return False
    except Exception as e:
        flash(f"Erro ao autenticar o usuário: {str(e)}", "danger")
        return None

# =================== Decorador: Verifica Autenticação ===================
def login_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not validar_acesso():
            return redirect(url_for('login_route.login'))
        return f(*args, **kwargs)
    return decorated_function

# =================== Decorador: Verifica Acesso Administrativo ===================
def admin_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not validar_acesso(nivel_requerido='admin'):
            return redirect(url_for('login_route.login'))
        return f(*args, **kwargs)
    return decorated_function
