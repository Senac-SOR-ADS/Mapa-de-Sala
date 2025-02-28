
import re
from datetime import datetime, timedelta
from App.view.feedback import Feedback

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


def sucessoEdicao(self):
    texto = 'Edição Feito Com Sucesso!'
    resposta = Feedback(True, texto, 'Sucesso!', 'Edição Concluido')
    if resposta.exec_():
        pass

def erroEdicao(self):
    texto = 'Erro Ao Fazer Edição!'
    resposta = Feedback(False, texto, 'Erro!', 'Aconteceu Algo De Errado Ao Fazer A Edição..')
    if resposta.exec_():
        pass

def sucessoCadastro(self):
    texto = 'Cadastro Feito Com Sucesso!'
    resposta = Feedback(True, texto, 'Sucesso!', 'Cadastro Concluido')
    if resposta.exec_():
        pass

def erroCadastro(self):
    texto = 'Erro Ao Fazer Cadastro!'
    resposta = Feedback(False, texto, 'Erro!', 'Aconteceu Algo De Errado Ao Fazer O Cadastro..')
    if resposta.exec_():
        pass


def listas_intervalo_dias(dataInicio:str, dataFim:str, dias_semana:list=[1,1,1,1,1,0,0])->list:
    """ Função para retornar listas de dias validos dentro do intervalo"""
    diaInicio = datetime.strptime(modificarDataReserva(dataInicio), "%d/%m/%Y")
    diaFim = datetime.strptime(modificarDataReserva(dataFim), "%d/%m/%Y")
    dia_atual = diaInicio
    lista_dias = []
    while dia_atual <= diaFim:
        if dias_semana[dia_atual.weekday()]:
            lista_dias.append(dia_atual.strftime("%Y/%m/%d"))
        dia_atual += timedelta(days=1)
    return lista_dias
