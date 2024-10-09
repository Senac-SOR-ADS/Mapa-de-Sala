from App.model.sala import Sala

def cadastrarSala(nome, tipo, predio, equipamento, capacidade, feedback):
    sala = Sala(nome, tipo, predio, equipamento, capacidade, feedback)
    if sala.cadastrar_sala():
        return True
    return False