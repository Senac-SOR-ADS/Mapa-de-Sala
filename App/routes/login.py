from flask import Blueprint, render_template, request, redirect, url_for, flash
from functools import wraps
from App.routes.acesso import validar_acesso, autenticar

# Definindo o blueprint para a rota de login
login_route = Blueprint('login_route', __name__, template_folder='templates')

# Decorator para verificar se o usuário está autenticado
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not validar_acesso():
            flash('Você precisa estar logado para acessar essa página.', 'error')
            return redirect(url_for('login_route.login'))
        return f(*args, **kwargs)
    return decorated_function

@login_route.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        senha = request.form.get("senha")
        if autenticar(email, senha):
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('home_route.home'))
        flash('Credenciais inválidas. Tente novamente.', 'error')
    elif request.method == 'GET' and validar_acesso():
        return redirect(url_for('home_route.home'))
    return render_template('login.html')
