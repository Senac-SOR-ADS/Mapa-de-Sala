import re

# =================== criada para controller Pessoa ===================

# Função para modificar a data  
def modificarData(dataNasc):
    data = dataNasc.split('/')
    return f'{data[2]}-{data[1]}-{data[0]}'

# Função para formatar o CPF
def formatarCpf(cpf):
    return re.sub(r'(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.\2.\3-\4', cpf)

# Função para formatar o CNPJ
def formatarCnpj(cnpj):
    return re.sub(r'(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})', r'\1.\2.\3/\4-\5', cnpj)

# Função para formatar o telefone
def formatarTelefone(telefone):
    return re.sub(r'(\d{2})(\d{4,5})(\d{4})', r'(\1) \2-\3', telefone)

# =================== criada para controller Sala ===================
def validarInputs(valores):
    for i in valores:
        if not i:
            return False
    return True

# =================== criada para controller Pessoa para Reserva ===================
def modificarDataReserva(data):
    data = data.split('-')
    return f'{data[2]}/{data[1]}/{data[0]}'