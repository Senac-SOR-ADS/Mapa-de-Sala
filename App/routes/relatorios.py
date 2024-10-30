from flask import render_template, Blueprint
from App.routes.auth.autenticar import login_auth
from App.controller.pessoa import buscaPessoas
from App.controller.curso import listarCursos
from App.controller.sala import listarSala

# Definindo o blueprint
relatorio_route = Blueprint('relatorio_route', __name__, template_folder='templates/Relatorios/')

@relatorio_route.route("/reservas", methods=['GET', 'POST'])
@login_auth
def listarReserva():
    salas = listarSala()
    pessoas = buscaPessoas()
    cursos = listarCursos()

    return render_template('/Relatorios/listarReservas.html', salas=salas, pessoas=pessoas, cursos=cursos)

@relatorio_route.route("/ocupado", methods=['GET', 'POST'])
@login_auth
def ocupadoEquipamento():
    return render_template('/Relatorios/ocupadoEquipamento.html')