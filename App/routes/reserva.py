from flask import render_template, Blueprint
from App.routes.auth.autenticar import login_auth
from App.controller.pessoa import buscarPessoas
from App.controller.sala import listarSala

# Definindo o blueprint
reserva_route = Blueprint('reserva_route', __name__, template_folder='templates/Reservas/')

@reserva_route.route("/", methods=['GET', 'POST'])
@login_auth
def cadastrar_Reserva():
    salas = listarSala()
    pessoas = buscarPessoas()
    return render_template('Reservas/cadastrar.html', salas=salas, pessoas=pessoas)
