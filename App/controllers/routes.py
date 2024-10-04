from App import app
from App.controllers import acesso
from flask import render_template

@app.route('/')
def main():
    if acesso.validarAcesso():
        return render_template('home.html')
    else:
        return render_template('Error404.html'), 404

@app.errorhandler(404)
def page_not_found(error):
    return render_template('Error404.html'), 404

@app.route("/login", methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route("/cadstrarArea", methods=['GET', 'POST'])
def cadastrarArea():
    return render_template('cadastrarArea.html')

@app.route("/cadastrarCurso", methods=['GET', 'POST'])
def cadastrarCurso():
    return render_template('cadastrarCurso.html')

@app.route("/cadastrarSalas", methods=['GET', 'POST'])
def cadastrarSalas():
    return render_template('cadastrarSalas.html')

@app.route("/cadastroPessoas", methods=['GET', 'POST'])
def cadastroPessoas():
    return render_template('cadastroPessoas.html')

@app.route("/reserva", methods=['GET', 'POST'])
def reserva():
    return render_template('reserva.html')

@app.route("/cadastrarEquipamentos", methods=['GET', 'POST'])
def cadastrarEquipamentos():
    return render_template('cadastrarEquipamentos.html')

@app.route("/relatorios", methods=['GET', 'POST'])
def relatorios():
    return render_template('relatorios.html') 

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    return render_template('logout.html')