from App.model.sala import Sala

def cadastrarSala(nome, tipo, predio, equipamento, capacidade, feedback):
    sala = Sala(nome, tipo, predio, equipamento, capacidade, feedback)
    if sala.cadastrar_sala():
        return True
    return False

def validarInputs(valores):
    for i in valores:
        if not i:
            return False
    return True

def listarSala():
    todasSalas = Sala.buscar_nomeId_sala()
    listarSalas = {i[1]:i[0] for i in todasSalas}
    return(listarSalas)