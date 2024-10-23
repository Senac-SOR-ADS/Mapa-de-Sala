from datetime import datetime, timedelta

def validarDia(diaInicio, diaFim, diasValidos):
    diaInicio = datetime.strptime(diaInicio, "%d/%m/%Y")
    diaFim = datetime.strptime(diaFim, "%d/%m/%Y")
    
    diaAtual = diaInicio
    
    while diaAtual <= diaFim:
        diaSemana = diaAtual.weekday()
        if diasValidos[diaSemana]:
            print(diaAtual.strftime("%d/%m/%Y"), diaSemana)
        diaAtual += timedelta(days=1)