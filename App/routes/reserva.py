from flask import render_template, Blueprint
from App.routes.login import login_required

# Definindo o blueprint
reserva_route = Blueprint('reserva_route', __name__, template_folder='templates/Reservas/')

@reserva_route.route("/", methods=['GET', 'POST'])
@login_required
def cadastrarReserva():
    return render_template('/Reservas/cadastrar.html')