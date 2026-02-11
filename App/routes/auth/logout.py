from flask import Blueprint, redirect, session, url_for
from App.routes.auth.acesso import remover_acesso

# Definindo o blueprint para a rota de logout
logout_route = Blueprint('logout_route', __name__, template_folder='templates/Login/')

@logout_route.route("/logout", methods=['GET'])
def logout():
    remover_acesso()
    session.pop('sessao_expirada', None)
    return redirect(url_for('login_route.login'))
