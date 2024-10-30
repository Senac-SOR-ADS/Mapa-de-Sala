from flask import render_template, Blueprint, redirect, url_for, flash, session
from App.routes.auth.autenticar import login_auth

# Definindo o blueprint para a rota de home
home_route = Blueprint('home_route', __name__, template_folder='templates/Home/')

@home_route.route('/', methods=['GET'])
@home_route.route('/home', methods=['GET'])
@login_auth
def home():
    """Rota para a página inicial, protegida por autenticação."""
    return render_template('/Home/home.html')

@home_route.app_errorhandler(404)
def page_not_found(error):
    """Tratamento de erro 404: Página não encontrada."""
    flash('Página não encontrada. Verifique o URL.', 'danger')
    return render_template('/Home/error404.html'), 404
