
from datetime import datetime, timedelta
from App.model.reserva import Reserva
from App.controller.utils import modificarDataReserva, listas_intervalo_dias
from App.model.curso import Curso

def realizar_reserva_no_dia(idLogin, dados, lista_de_dias):
    for diaAtual in lista_de_dias:
        Reserva(idLogin, dados['idDocente'], dados['idCurso'], dados['idSala'], diaAtual, dados['inicioCurso'], dados['fimCurso'], 0, dados['observações']).fazer_reserva()
    return True

def validarCadastro(dados, diasValidos)->list|None:
    lista_de_dias = listas_intervalo_dias(dados['diaInicio'], dados['diaFim'], diasValidos)
    dias_livres = []
    dias_ocupados = {}
    for diaAtual in lista_de_dias:
        validar = Reserva.validar_periodo(dados['idSala'], diaAtual, dados['inicioCurso'], dados['fimCurso'])
        if validar:
            #lista_de_dias.remove(diaAtual)
            reserva_ocupada = validar[0]
            info_curso = Curso.retorna_todas_infos_curso(reserva_ocupada[3])
            dias_ocupados[diaAtual] = (reserva_ocupada, info_curso)
        else:
            dias_livres.append(diaAtual)
    return (dias_livres, dias_ocupados)


def trocar_reserva(dados1, dados2):
    if Reserva.atualizar(dados1['idLogin'], dados1['idPessoa'], dados1['idcurso'], dados1['idSala'], dados1['dia'], dados1['inicioCurso'], dados1['fimCurso'], dados1['observações'],  dados1['idReserva']):
        Reserva.atualizar(dados2['idLogin'], dados2['idPessoa'], dados2['idcurso'], dados2['idSala'], dados2['dia'], dados2['inicioCurso'], dados2['fimCurso'], dados2['observações'],  dados2['idReserva'])


def atualizarReserva(idLogin, idPessoa, idCurso, idSala, dia, hrInicio, hrFim, observacao, idReserva):
    if Reserva.atualizar(idLogin, idPessoa, idCurso, idSala, dia, hrInicio, hrFim, observacao, idReserva):
        return True
    return False

def validarDiaSemana(dia, diaSemana):
    formatoDia = modificarDataReserva(dia)
    formatoDia = datetime.strptime(formatoDia, "%d/%m/%Y")
    dia = datetime.weekday(formatoDia)
    if diaSemana[dia]:
        return True
    print('Selecione o dia da semana certo!')
    return False
