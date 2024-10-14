from flask import render_template, Blueprint, request, redirect, url_for, flash
from App.routes.acesso import *
from functools import wraps

# Definindo o blueprint
routes = Blueprint('routes', __name__)

# Decorator para verificar se o usuário está autenticado
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not validar_acesso():
            flash('Você precisa estar logado para acessar essa página.', 'error')
            return redirect(url_for('routes.login'))
        return f(*args, **kwargs)
    return decorated_function

@routes.route('/', methods=['GET'])
@routes.route('/home', methods=['GET'])
@login_required
def home():
    return render_template('home.html')

@routes.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html'), 404

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form["email"]
        senha = request.form["senha"]
        if autenticar(email, senha):
            return redirect(url_for('routes.home'))
        flash('Credenciais inválidas. Tente novamente.', 'error')
    elif request.method == 'GET':
        if validar_acesso():
            return redirect(url_for('routes.home'))
    return render_template('login.html')

@routes.route("/logout")
def logout():
    session.pop('user', None)
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('routes.login'))