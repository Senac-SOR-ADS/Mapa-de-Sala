from flask import render_template, Blueprint
from App.routes.login import login_required

# Definindo o blueprint
reserva_route = Blueprint('reserva_route', __name__, template_folder='templates')

@reserva_route.route("/", methods=['GET', 'POST'])
@login_required
def reserva():
    return render_template('reserva.html')

@reserva_route.route("/relatorio", methods=['GET', 'POST'])
@login_required
def relatorioReserva():
    return render_template('relatorioReserva.html')