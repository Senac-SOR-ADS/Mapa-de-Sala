from flask import session, flash
from App.controller.login import pegarUsuarioLogado, removerUsuarioLogado

def validar_acesso():
    """Verifica se o usuário está autenticado."""
    if 'user' in session:
        return True
    return False

def registrar_acesso():
    session['user'] = pegarUsuarioLogado()

def remover_acesso():
    removerUsuarioLogado()
    session.pop('user', None)

def pegar_acesso():
    return session.get('user')