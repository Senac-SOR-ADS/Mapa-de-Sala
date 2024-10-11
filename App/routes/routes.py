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
        email = request.form.get("email")
        senha = request.form.get("senha")
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

@routes.route("/area", methods=['GET', 'POST'])
@login_required
def area():
    return render_template('area.html')

@routes.route("/curso", methods=['GET', 'POST'])
@login_required
def curso():
    return render_template('curso.html')

@routes.route("/equipamento", methods=['GET', 'POST'])
@login_required
def equipamentos():
    return render_template('equipamento.html')

@routes.route("/funcionario", methods=['GET', 'POST'])
@login_required
def funcionario():
    return render_template('funcionario.html')

@routes.route("/relatorioReserva", methods=['GET', 'POST'])
@login_required
def relatorioReserva():
    return render_template('relatorioReserva.html')

@routes.route("/reserva", methods=['GET', 'POST'])
@login_required
def reserva():
    return render_template('reserva.html')

@routes.route("/sala", methods=['GET', 'POST'])
@login_required
def sala():
    return render_template('sala.html')

@routes.route("/cadastrarSala", methods=['GET', 'POST'])
@login_required
def cadastrarSala():
    return render_template('cadastrarSala.html')

@routes.route("/cadastrarArea", methods=['GET', 'POST'])
@login_required
def cadastrarArea():
    return render_template('cadastrarArea.html')

@routes.route("/cadastrarCurso", methods=['GET', 'POST'])
@login_required
def cadastrarCurso():
    return render_template('cadastrarCurso.html')  

@routes.route("/cadastrarEquipamento", methods=['GET', 'POST'])
@login_required
def cadastrarEquipamento():
    return render_template('cadastrarEquipamento.html')

@routes.route("/cadastrarFuncionario", methods=['GET', 'POST'])
@login_required
def cadastrarFuncionario():
    return render_template('cadastrarFuncionario.html')

@routes.route("/ocupadoEquipamento", methods=['GET', 'POST'])
@login_required
def ocupadoEquipamento():
    return render_template('ocupadoEquipamento.html')