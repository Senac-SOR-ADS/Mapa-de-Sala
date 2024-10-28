from flask import Blueprint, redirect, url_for, flash, session

# Definindo o blueprint para a rota de logout
logout_route = Blueprint('logout_route', __name__, template_folder='templates/Login/')

@logout_route.route("/logout", methods=['GET', 'POST'])
def logout():
    """Rota para realizar logout do usuário."""
    session.pop('user', None)
    flash('Você foi desconectado com sucesso! Até logo!', 'success')
    return redirect(url_for('login_route.login'))
