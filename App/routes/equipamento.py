from flask import render_template, Blueprint
from App.routes.auth.autenticar import login_auth
from App.controller.area import listarAreas

# Definindo o blueprint
equipamento_route = Blueprint('equipamento_route', __name__, template_folder='templates/Equipamentos/')

@equipamento_route.route("/", methods=['GET', 'POST'])
@login_auth
def listarEquipamento():
    return render_template('/Equipamentos/listar.html')

@equipamento_route.route("/cadastrar", methods=['GET', 'POST'])
@login_auth
def cadastrarEquipamento():
    areas = listarAreas()
    return render_template('/Equipamentos/cadastrar.html', areas=areas)

@equipamento_route.route('/editar/<int:id>', methods=['GET'])
@login_auth
def EditarEquipamento():
    return render_template('/Equipamentos/editar.html')