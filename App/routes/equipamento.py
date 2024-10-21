from flask import render_template, Blueprint
from App.routes.login import login_required

# Definindo o blueprint
equipamento_route = Blueprint('equipamento_route', __name__, template_folder='templates/Equipamentos/')

@equipamento_route.route("/", methods=['GET', 'POST'])
@login_required
def listarEquipamentos():
    return render_template('/Equipamentos/listar.html')

@equipamento_route.route("/cadastrar", methods=['GET', 'POST'])
@login_required
def cadastrarEquipamento():
    return render_template('/Equipamentos/cadastrar.html')

@equipamento_route.route('/editar/<int:id>', methods=['GET'])
@login_required
def EditarEquipamento():
    return render_template('/Equipamentos/editar.html')