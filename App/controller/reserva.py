from datetime import datetime, timedelta
from App.model.reserva import Reserva
from App.controller.utils import modificarDataReserva

def fazendoReserva(idLogin, dados, diasValidos):
    diaInicio = modificarDataReserva(dados['diaInicio'])
    diaInicio = datetime.strptime(diaInicio, "%d/%m/%Y")
    diaFim = modificarDataReserva(dados['diaFim'])
    diaFim = datetime.strptime(diaFim, "%d/%m/%Y")
    diaAtual = diaInicio
    
    while diaAtual <= diaFim:
        diaSemana = diaAtual.weekday()
        if diasValidos[diaSemana]:
            Reserva(idLogin, dados['idDocente'], dados['idCurso'], dados['idSala'], diaAtual, dados['inicioCurso'], dados['fimCurso'], dados['observações']).fazer_reserva()
        diaAtual += timedelta(days=1)
    print('Reserva feita com sucesso!')
    return True
        
def validarCadastro(idLogin, dados, diasValidos):
    diaInicio = modificarDataReserva(dados['diaInicio'])
    diaInicio = datetime.strptime(diaInicio, "%d/%m/%Y")
    diaFim = modificarDataReserva(dados['diaFim'])
    diaFim = datetime.strptime(diaFim, "%d/%m/%Y")
    diaAtual = diaInicio
    
    while diaAtual <= diaFim:
        diaSemana = diaAtual.weekday()
        if diasValidos[diaSemana]:
            if not Reserva(idLogin, dados['idDocente'], dados['idCurso'], dados['idSala'], diaAtual, dados['inicioCurso'], dados['fimCurso'], dados['observações']).validar_periodo():
                print(f'Na seguinte data já existe uma reserva: {diaAtual}')
                return False
        diaAtual += timedelta(days=1)
    print('Todos os dias estão livres')
    return True

def trocar_reserva(dados1, dados2):
    if Reserva.atualizar(dados1['idLogin'], dados1['idPessoa'], dados1['idcurso'], dados1['idSala'], dados1['dia'], dados1['inicioCurso'], dados1['fimCurso'], dados1['observações'],  dados1['idReserva']):
        Reserva.atualizar(dados2['idLogin'], dados2['idPessoa'], dados2['idcurso'], dados2['idSala'], dados2['dia'], dados2['inicioCurso'], dados2['fimCurso'], dados2['observações'],  dados2['idReserva'])
        
        
    
def deletarReserva(idReserva):
    if Reserva.deletar(idReserva):
        return True
    return False

def atualizarReserva(idLogin, idPessoa, idCurso, idSala, dia, hrInicio, hrFim, observacao, idReserva):
    if Reserva.atualizar(idLogin, idPessoa, idCurso, idSala, dia, hrInicio, hrFim, observacao, idReserva):
        return True
    return False

