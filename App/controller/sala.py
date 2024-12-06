from App.model.sala import Sala

def cadastrarSala(nome, tipo, predio, equipamento, capacidade, feedback):
    sala = Sala(nome, tipo, predio, equipamento, capacidade, feedback)
    if sala.cadastrar_sala():
        return True
    return False

def listarSala():
    todasSalas = Sala.buscar_nomeId_sala()
    listarSalas = {i[1]:i[0] for i in todasSalas}
    return(listarSalas)

def atualizarSala(nome, tipo, predio, equipamento, capacidade, observacao, idSala):
    if Sala.atualizar(nome, tipo, predio, equipamento, capacidade, observacao, idSala):
        return True
    return False
    
def buscarSalaId(idSala):
    if not isinstance(idSala, int):
        return {"error": "ID inválido. Deve ser um número inteiro."}
    try:
        resultado = Sala.pesquisar_id(idSala)
        if not resultado or len(resultado) < 5:
            return {"error": "Sala não encontrado"}

        return {
            "idSala": resultado[0],
            "nome": resultado[1],
            "tipo": resultado[2],
            "predio": resultado[3],
            "equipamentos": resultado[4],
            "capacidade": resultado[5],
            "observacao": resultado[6],
            }
    except Exception as e:
        return {"error": f"Erro ao buscar sala: {e}"}

def deletarSala(idSala):
    if Sala.deletar(idSala):
        return True
    return False