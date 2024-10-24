from flask import session, flash

def validar_acesso():
    """Verifica se o usuário está autenticado."""
    if 'user' in session:
        return True
    return False
