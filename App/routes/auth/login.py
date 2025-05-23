import os
import random
from flask import Blueprint, render_template, request, redirect, url_for
from App.routes.auth.autenticar import validar_acesso, autenticar

# Definindo o blueprint para a rota de login
login_route = Blueprint('login_route', __name__, template_folder='templates/Login/')

@login_route.route('/', methods=['GET', 'POST'])
def login():
    
    # Caminho da pasta de imagens
    img_folder = 'App/static/img/login/'
    
    # Listando todas as imagens na pasta
    try:
        images = [f for f in os.listdir(img_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    except FileNotFoundError:
        images = []

    # Selecionando uma imagem aleatória ou definindo uma imagem padrão
    random_image = random.choice(images) if images else 'default.jpg'
    
    if request.method == 'POST':
        email = request.form.get("email")
        senha = request.form.get("senha")
        if autenticar(email, senha):
            return redirect(url_for('home_route.home'))
    
    elif request.method == 'GET' and validar_acesso():
        return redirect(url_for('home_route.home'))
    
    # Renderizando o template com a imagem aleatória
    return render_template('Login/login.html', image=random_image)
