from flask import render_template, Blueprint, request
from App.controller.login import validarLogin

# Definindo o blueprint
routes = Blueprint('routes', __name__)

@routes.route('/')
@routes.route('/home')
def main():
    return render_template('home.html')

@routes.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html'), 404

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form["email"]
        senha = request.form["senha"]
        if validarLogin(email, senha):
            print('redirecionar rota para home')
            return render_template('home.html')
        else:
            print('nao deu..')
    return render_template('login.html')