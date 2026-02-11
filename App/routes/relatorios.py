import datetime
from flask import render_template, Blueprint, request
from App.routes.auth.autenticar import login_auth
from App.controllerWeb.relatorio import pesquisarDia
from App.model.logger import logger

# Definindo o blueprint
relatorio_route = Blueprint('relatorio_route', __name__, template_folder='templates/Relatorios/')

@relatorio_route.route("/relatorio", methods=['GET', 'POST'])
@login_auth
def listar_Relatorio():
    hoje = datetime.date.today()
    data_selecionada = request.args.get("data", str(hoje))

    try:
        data_formatada = datetime.datetime.strptime(data_selecionada, "%Y-%m-%d").date()
    except ValueError:
        logger.warning(f"Data inválida informada: {data_selecionada}")
        return render_template('/Relatorios/listarDia.html', reservas=[], hoje=hoje)

    reservas_formatadas = pesquisarDia(data_formatada)

    if reservas_formatadas:
        logger.info(f"{len(reservas_formatadas)} reservas encontradas para {data_formatada}.")
    else:
        logger.warning(f"Nenhuma reserva encontrada para {data_formatada}.")

    # Corrigido o nome da variável para 'reservas' e passando os dados corretamente.
    return render_template('/Relatorios/listarDia.html', reservas=reservas_formatadas, hoje=hoje)

