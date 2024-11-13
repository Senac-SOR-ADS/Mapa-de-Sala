from flask import Blueprint, render_template, request, redirect, url_for, flash
from App.routes.auth.autenticar import validar_acesso, autenticar

# Definindo o blueprint para a rota de login
login_route = Blueprint('login_route', __name__, template_folder='templates/Login/')

@login_route.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        senha = request.form.get("senha")
        if autenticar(email, senha):
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('home_route.home'))
        flash('Credenciais inválidas. Verifique seu e-mail e senha e tente novamente.', 'error')
    
    elif request.method == 'GET' and validar_acesso():
        return redirect(url_for('home_route.home'))
    
    return render_template('Login/login.html')
