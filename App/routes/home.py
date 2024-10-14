from flask import render_template, Blueprint, redirect, url_for, flash, session
from App.routes.login import login_required

# Definindo o blueprint para a rota de home
home_route = Blueprint('home_route', __name__, template_folder='templates')

@home_route.route('/', methods=['GET'])
@home_route.route('/home', methods=['GET'])
@login_required
def home():
    """Rota para a página inicial, protegida por autenticação."""
    return render_template('home.html')

@home_route.app_errorhandler(404)
def page_not_found(error):
    """Tratamento de erro 404: Página não encontrada."""
    return render_template('error404.html'), 404

@home_route.route("/logout", methods=['GET', 'POST'])
def logout():
    """Rota para realizar logout do usuário."""
    session.pop('user', None)
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('login_route.login'))
