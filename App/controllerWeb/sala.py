from App.model.sala import Sala
from App.model.logger import logger

# =================== cadastrar ===================
def cadastrarSala(nome: str, tipo: str, predio: str, equipamento: str, capacidade: int, observacao: str) -> dict:
    """Cadastra uma nova sala no banco de dados."""
    try:
        sala = Sala(nome, tipo, predio, equipamento, capacidade, observacao)
        
        if sala.cadastrar_sala():
            return {"success": "Sala cadastrada com sucesso."}
        return {"error": "Não foi possível cadastrar a sala."}
    except Exception as e:
        logger.error("Erro ao cadastrar sala: %s", str(e))
        return {"error": "Erro ao cadastrar sala."}

# =================== atualizar ===================
def atualizarSala(nome: str, tipo: str, predio: str, equipamento: str, capacidade: int, observacao: str, idSala: int) -> dict:
    """Atualiza os dados de uma sala existente no banco de dados."""
    try:
        if Sala.atualizar(nome, tipo, predio, equipamento, capacidade, observacao, idSala):
            return {"success": "Sala atualizada com sucesso."}
        return {"error": "Falha ao atualizar os dados da sala."}
    except Exception as e:
        logger.error("Erro ao atualizar sala ID %d: %s", idSala, str(e))
        return {"error": "Erro ao atualizar sala."}

# =================== listar ===================
def listarSala(search_query: str = '') -> dict:
    """Retorna um dicionário com todas as salas cadastradas.
    Filtra os resultados com base no nome ou tipo se a query de pesquisa for fornecida."""
    try:
        todasSalas = Sala.buscar_sala()

        if search_query:
            todasSalas = [
                sala for sala in todasSalas if search_query.lower() in sala.get_nome().lower() or search_query.lower() in sala.tipo.lower()
            ]
        
        return {sala.get_nome(): sala.get_id() for sala in todasSalas} if todasSalas else {}
    except Exception as e:
        logger.error("Erro ao listar salas: %s", str(e))
        return {"error": "Erro ao listar salas."}

# =================== remover ===================
def removerSala(idSala: int) -> dict:
    """Remove uma sala do banco de dados pelo ID."""
    try:
        if Sala.deletar(idSala):
            return {"success": "Sala removida com sucesso."}
        return {"error": "Não foi possível remover a sala."}
    except Exception as e:
        logger.error("Erro ao remover sala ID %d: %s", idSala, str(e))
        return {"error": "Erro ao remover sala."}

# =================== buscar por ID ===================
def buscarSalaId(idSala: int) -> dict:
    """Busca uma sala pelo ID e retorna suas informações ou uma mensagem de erro se não for encontrada."""
    if not isinstance(idSala, int):
        return {"error": "ID inválido. Deve ser um número inteiro."}
    try:
        resultado = Sala.pesquisar_id(idSala)

        if not resultado:
            return {"error": "Sala não encontrada"}

        return {
            "idSala": resultado[0],
            "nome": resultado[1],
            "tipo": resultado[2],
            "predio": resultado[3],
            "equipamentos": resultado[4] or None,
            "capacidade": resultado[5],
            "observacao": resultado[6] or None,
        }
    except Exception as e:
        logger.error("Erro ao buscar sala ID %d: %s", idSala, str(e))
        return {"error": "Erro ao buscar sala."}
