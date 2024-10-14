from flask import render_template, Blueprint
from App.routes.login import login_required

# Definindo o blueprint
equipamento_route = Blueprint('equipamento_route', __name__, template_folder='templates')

@equipamento_route.route("/", methods=['GET', 'POST'])
@login_required
def equipamentos():
    return render_template('equipamento.html')

@equipamento_route.route("/cadastrar", methods=['GET', 'POST'])
@login_required
def cadastrarEquipamento():
    return render_template('cadastrarEquipamento.html')

@equipamento_route.route("/ocupado", methods=['GET', 'POST'])
@login_required
def ocupadoEquipamento():
    return render_template('ocupadoEquipamento.html')