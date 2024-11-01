from datetime import datetime, timedelta
from App.model.reserva import Reserva
from App.controller.pessoa import modificarDataReserva

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
            if not Reserva(idLogin, dados['idDocente'], dados['idCurso'], dados['idSala'], diaAtual, dados['inicioCurso'], dados['fimCurso'], dados['observações']).validar_dia_livre():
                print(f'Na seguinte data já existe uma reserva: {diaAtual}')
                return False
        diaAtual += timedelta(days=1)
    print('Todos os dias estão livres')
    return True