from flask import render_template, Blueprint
from App.routes.login import login_required

# Definindo o blueprint
relatorio_route = Blueprint('relatorio_route', __name__, template_folder='templates/Relatorios/')

@relatorio_route.route("/reservas", methods=['GET', 'POST'])
@login_required
def listarReserva():
    return render_template('/Relatorios/listarReservas.html')

@relatorio_route.route("/ocupado", methods=['GET', 'POST'])
@login_required
def ocupadoEquipamento():
    return render_template('/Relatorios/ocupadoEquipamento.html')