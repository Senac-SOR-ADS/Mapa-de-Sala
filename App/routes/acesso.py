from App.controller.login import validarLogin
from flask import session

def validar_acesso():
    """Verifica se o usuário está autenticado."""
    return 'user' in session

def autenticar(username, password):
    """Autentica um usuário verificando suas credenciais."""
    try:
        if validarLogin(username, password):
            session['user'] = username
            return True
    except Exception as e:
        print(f"Erro ao verificar credenciais: {e}")
    return False
