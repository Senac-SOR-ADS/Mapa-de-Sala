from flask import flash
from App.model.reserva import Reserva
from App.controllerWeb.utils import listas_intervalo_dias
from App.model.curso import Curso
from App.model.logger import logger
from typing import List, Tuple, Dict, Optional

def realizar_reserva_no_dia(idLogin, dados, lista_de_dias):
    try:
        for diaAtual in lista_de_dias:
            reserva = Reserva(idLogin, dados['idDocente'], dados['idCurso'], dados['idSala'], diaAtual, dados['inicioCurso'], dados['fimCurso'], 0, dados['observações'])
            reserva.fazer_reserva()
        return True
    except Exception as e:
        logger.error(f"Erro ao tentar realizar a reserva: {str(e)}")
        return False


def validarCadastro(dados, diasValidos) -> Optional[Tuple[List[str], Dict[str, Tuple]]]:
    lista_de_dias = listas_intervalo_dias(dados['diaInicio'], dados['diaFim'], diasValidos)
    dias_livres = []
    dias_ocupados = {}

    try:
        for diaAtual in lista_de_dias:
            validar = Reserva.validar_periodo(dados['idSala'], diaAtual, dados['inicioCurso'], dados['fimCurso'])
            if validar:
                reserva_ocupada = validar[0]
                info_curso = Curso.retorna_todas_infos_curso(reserva_ocupada[3])
                dias_ocupados[diaAtual] = (reserva_ocupada, info_curso)
                logger.warning(f"Sala {dados['idSala']} já está ocupada no dia {diaAtual} para o curso {info_curso}. Horário: {dados['inicioCurso']} - {dados['fimCurso']}")
                flash(f"Sala {dados['idSala']} já está ocupada no dia {diaAtual} para o curso {info_curso}. Horário: {dados['inicioCurso']} - {dados['fimCurso']}", "warning")
            else:
                dias_livres.append(diaAtual)

    except Exception as e:
        logger.error(f"Erro ao verificar disponibilidade para o dia {diaAtual}. Detalhes: {str(e)}")

    return (dias_livres, dias_ocupados)


def trocar_reserva(dados1, dados2):
    try:
        if Reserva.atualizar(**dados1) and Reserva.atualizar(**dados2):
            logger.info(f"Troca de reservas feita! ID 1: {dados1['idReserva']}, ID 2: {dados2['idReserva']}, Salas: {dados1['idSala']} ↔ {dados2['idSala']}, Datas: {dados1['dia']} ↔ {dados2['dia']}")
        else:
            logger.warning(f"Falha ao trocar as reservas: {dados1['idReserva']} ↔ {dados2['idReserva']}")
    except Exception as e:
        logger.error(f"Erro ao tentar trocar reservas. Detalhes: {str(e)}")


def atualizarReserva(idLogin, idPessoa, idCurso, idSala, dia, hrInicio, hrFim, observacao, idReserva):
    try:
        if Reserva.atualizar(idLogin, idPessoa, idCurso, idSala, dia, hrInicio, hrFim, observacao, idReserva):
            logger.info(f"Reserva atualizada com sucesso! ID {idReserva}, Usuário {idLogin}, Data {dia}, Sala {idSala}, Horário {hrInicio} - {hrFim}, Obs: {observacao}")
            return True
        else:
            logger.warning(f"Falha ao atualizar reserva! ID {idReserva}, Usuário {idLogin}, Sala {idSala}, Data {dia}, Horário {hrInicio} - {hrFim}")
            return False
    except Exception as e:
        logger.error(f"Erro ao tentar atualizar reserva. Detalhes: {str(e)}")
        return False



def verificarPesquisa(dados):
    filtros = {
        (True, False, False, False, False): Reserva.buscar_data,  
        (True, True, False, False, False): Reserva.buscar_data_oferta,  
        (True, False, False, False, True): Reserva.buscar_data_sala,  
        (True, False, False, True, False): Reserva.buscar_data_periodo,
        (True, False, False, True, True): Reserva.buscar_periodo_sala,
        (True, True, False, False, True): Reserva.buscar_oferta_sala,
        (True, True, False, True, False): Reserva.buscar_data_periodo_oferta,
        (True, True, False, True, True): Reserva.buscar_periodo_sala_oferta
    }

    chave = (
        bool(dados.get('dataInicio')) and bool(dados.get('dataFim')),
        bool(dados.get('oferta')),
        bool(dados.get('horaInicio')),
        bool(dados.get('horaFim')),
        bool(dados.get('sala'))
    )

    func = filtros.get(chave)
    
    if func:
        logger.info(f"Pesquisa realizada! Parâmetros utilizados: {dados}")

        # Recuperando os valores e garantindo que nenhum argumento essencial seja None
        dataInicio = dados.get('dataInicio')
        dataFim = dados.get('dataFim')
        oferta = dados.get('oferta', None)
        sala = dados.get('sala', None)
        horaInicio = dados.get('horaInicio', None)
        horaFim = dados.get('horaFim', None)

        if func == Reserva.buscar_data:
            return func(dataInicio, dataFim)  

        elif func == Reserva.buscar_data_oferta:
            return func(dataInicio, dataFim, oferta)

        elif func == Reserva.buscar_data_sala:
            return func(dataInicio, dataFim, sala)

        elif func == Reserva.buscar_data_periodo:
            return func(dataInicio, dataFim, horaInicio, horaFim)

        elif func == Reserva.buscar_periodo_sala:
            return func(dataInicio, dataFim, sala, horaInicio, horaFim)

        elif func == Reserva.buscar_oferta_sala:
            return func(dataInicio, dataFim, oferta, sala)

        elif func == Reserva.buscar_data_periodo_oferta:
            return func(dataInicio, dataFim, oferta, horaInicio, horaFim)

        elif func == Reserva.buscar_periodo_sala_oferta:
            return func(dataInicio, dataFim, oferta, sala, horaInicio, horaFim)

    logger.warning(f"Nenhum critério de pesquisa encontrado! Dados recebidos: {dados}")
    return None







