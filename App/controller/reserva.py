from datetime import datetime, timedelta

def validarDia(diaInicio, diaFim):
    diaInicio = datetime.strptime(diaInicio, "%d/%m/%Y")
    diaFim = datetime.strptime(diaFim, "%d/%m/%Y")
    
    diaAtual = diaInicio
    
    while diaAtual <= diaFim:
        diaSemana = diaAtual.weekday()
        if diaSemana in [0, 1, 2, 3, 4]:
            print(diaAtual.strftime("%d/%m/%Y"), diaSemana)
        diaAtual += timedelta(days=1)