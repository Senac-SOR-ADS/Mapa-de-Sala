# criada para controller Sala
def validarInputs(valores):
    for i in valores:
        if not i:
            return False
    return True

# criada para controller Pessoa
def modificarData(dataNasc):
    data = dataNasc.split('/')
    return f'{data[2]}-{data[1]}-{data[0]}'

# criada para controller Pessoa para Reserva
def modificarDataReserva(data):
    data = data.split('-')
    return f'{data[2]}/{data[1]}/{data[0]}'

# Validar ação
def validarAcao():
    print("ok")