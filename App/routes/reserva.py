from flask import flash, render_template, request, Blueprint
from App.routes.auth.autenticar import admin_suporte_auth, login_auth
from App.controllerWeb.pessoa import buscarPessoas
from App.controllerWeb.sala import listarSala
from App.controllerWeb.curso import listarCursos
from App.controllerWeb.equipamento import listarEquipamentos
from App.controllerWeb.reserva import realizar_reserva_no_dia, validarCadastro, trocar_reserva, atualizarReserva, verificarPesquisa
from App.controllerWeb.login import pegarUsuarioLogado
from App.model.logger import logger

# Definindo o blueprint
reserva_route = Blueprint('reserva_route', __name__, template_folder='templates/Reservas/')

def obter_dados_reserva():
    return {
        'pessoas': buscarPessoas(),
        'salas': listarSala(),
        'cursos': listarCursos(),
        'equipamentos': listarEquipamentos()
    }

def validar_usuario(usuario_logado, valores):
    if not usuario_logado or not usuario_logado.get('id_pessoa'):
        return False
    return True

def validar_pessoa(dados, valores):
    id_pessoa_form = int(dados.get('idPessoa', 0))
    if id_pessoa_form not in valores['pessoas'].values():
        return False
    return True

def validar_dias_semana(diasSemana, valores):
    if not diasSemana:
        return False

    diasSemana = [dia if dia in diasSemana else 'domingo_nao_marcado' for dia in ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']]
    return diasSemana

def processar_dados_reserva(dados, diasSemana):
    dados.update({
        'idDocente': int(dados.get('idPessoa', 0)),
        'idSala': int(dados['idSala']),
        'idCurso': int(dados['curso']),
        'idEquipamento': int(dados.get('idEquipamento', 0)),
        'diaInicio': dados['dataInicio'],
        'diaFim': dados['dataFim'],
        'inicioCurso': dados['horaInicio'],
        'fimCurso': dados['horaFim'],
        'observações': dados.get('observacao', '')
    })
    return validarCadastro(dados, diasSemana)


@reserva_route.route("/cadastrar", methods=['GET', 'POST'])
@admin_suporte_auth
def cadastrar_Reserva():
    valores = obter_dados_reserva()

    if request.method == 'POST':
        dados = request.form.to_dict()
        usuario_logado = pegarUsuarioLogado()

        if not validar_usuario(usuario_logado, valores):
            flash("Usuário não autenticado. Por favor, faça login para realizar a reserva.", "warning")
            logger.warning(f"Usuário não autenticado: {usuario_logado}")
            return render_template('Reservas/cadastrar.html', **valores)

        dados['idLogin'] = usuario_logado['id_pessoa']

        if not validar_pessoa(dados, valores):
            flash("Pessoa inválida selecionada para a reserva. Verifique os dados e tente novamente.", "warning")
            logger.warning(f"Pessoa inválida selecionada para reserva: {dados}")
            return render_template('Reservas/cadastrar.html', **valores)

        diasSemana = request.form.getlist('diasSemana[]')
        diasSemana = validar_dias_semana(diasSemana, valores)
        if not diasSemana:
            flash("Dias da semana inválidos ou não selecionados. Por favor, selecione dias válidos.", "warning")
            logger.warning(f"Dias da semana inválidos ou não selecionados: {diasSemana}")
            return render_template('Reservas/cadastrar.html', **valores)

        try:
            dias_livres, dias_ocupados = processar_dados_reserva(dados, diasSemana)

            if not dias_livres or len(dias_livres) == 0:
                flash(f"Não há dias livres para a reserva. Dias ocupados: {', '.join(dias_ocupados.keys())}", "warning")
                logger.warning(f"Não há dias livres para a reserva. Dias ocupados: {dias_ocupados}")
                return render_template('Reservas/cadastrar.html', **valores)

            for dia in dias_livres:
                sucesso = realizar_reserva_no_dia(dados['idLogin'], dados, [dia])
                if not sucesso:
                    flash(f"Falha ao realizar a reserva para o dia {dia}.", "error")
                    logger.error(f"Falha ao realizar a reserva para o dia {dia}.")
                    return render_template('Reservas/cadastrar.html', **valores)

            flash(f"Reservas realizadas com sucesso para os dias: {', '.join(dias_livres)}", "success")
            logger.info(f"Reservas realizadas com sucesso para o usuário {dados['idLogin']}, dias: {dias_livres}")
            return render_template('Reservas/cadastrar.html', **valores)

        except Exception as e:
            flash(f"Erro ao processar a reserva: {str(e)}", "error")
            logger.error(f"Erro ao processar a reserva: {str(e)}")
            return render_template('Reservas/cadastrar.html', **valores)

    return render_template('Reservas/cadastrar.html', pessoas=valores['pessoas'], salas=valores['salas'], cursos=valores['cursos'], equipamentos=valores['equipamentos'])



@reserva_route.route("/pesquisaUnitaria", methods=['GET', 'POST'])
@login_auth
def pesquisar_Unitaria():
    salas = listarSala()
    resultados = None
    search_query = None

    if request.method == 'POST':
        dados_pesquisa = request.form.to_dict()
        search_query = dados_pesquisa.get('search', '').strip()

        resultados = verificarPesquisa(dados_pesquisa)

        if not resultados:
            flash("Nenhum resultado encontrado para os critérios informados.", "warning")
        else:
            flash(f"Pesquisa realizada com sucesso! Encontrados {len(resultados)} resultado(s).", "success")

    return render_template('Reservas/pesquisaUnitaria.html', 
                           salas=salas, 
                           resultados=resultados,
                           search_query=search_query)

@reserva_route.route("/pesquisamultipla", methods=['GET', 'POST'])
@login_auth
def pesquisar_Multipla():
    return render_template('Reservas/pesquisamultipla.html')


@reserva_route.route("/trocar_reserva", methods=['POST'])
@admin_suporte_auth
def trocar_reserva_route():
    try:
        dados1 = request.form.to_dict()
        dados2 = request.form.to_dict()

        if trocar_reserva(dados1, dados2):
            flash("Troca de reservas realizada com sucesso!", "success")
            logger.info(f"Troca de reservas realizada com sucesso!")
            return render_template('Reservas/trocar_reserva.html')
        else:
            flash("Falha ao trocar as reservas. Verifique os dados e tente novamente.", "error")
            logger.warning(f"Falha ao trocar as reservas: {dados1['idReserva']} ↔ {dados2['idReserva']}")
            return render_template('Reservas/trocar_reserva.html')

    except Exception as e:
        flash(f"Erro ao trocar as reservas: {str(e)}", "error")
        logger.error(f"Erro ao trocar as reservas: {str(e)}")
        return render_template('Reservas/trocar_reserva.html')


@reserva_route.route("/atualizar_reserva", methods=['POST'])
@admin_suporte_auth
def atualizar_reserva_route():
    try:
        dados = request.form.to_dict()

        if atualizarReserva(dados['idLogin'], dados['idPessoa'], dados['idCurso'], dados['idSala'], dados['dia'], dados['horaInicio'], dados['horaFim'], dados['observacao'], dados['idReserva']):
            flash("Reserva atualizada com sucesso!", "success")
            logger.info(f"Reserva atualizada com sucesso!")
            return render_template('Reservas/atualizar_reserva.html')
        else:
            flash("Falha ao atualizar a reserva. Verifique os dados e tente novamente.", "error")
            logger.warning(f"Falha ao atualizar a reserva: {dados['idReserva']}")
            return render_template('Reservas/atualizar_reserva.html')

    except Exception as e:
        flash(f"Erro ao atualizar a reserva: {str(e)}", "error")
        logger.error(f"Erro ao atualizar a reserva: {str(e)}")
        return render_template('Reservas/atualizar_reserva.html')
