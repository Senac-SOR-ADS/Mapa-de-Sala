from App.model.equipamentos import Equipamentos
from App.model.logger import logger

# =================== cadastrar ===================
def cadastrarEquipamento(idArea: int, dados: dict) -> dict:
    """ Cadastra um novo equipamento associado a uma área no banco de dados. """
    try:
        equipamentoModel = Equipamentos(dados['nome'], dados['marca'], dados['quantidade'], idArea)
        resultado_cadastro = equipamentoModel.cadastrar_equipamento(idArea)
        
        if resultado_cadastro:
            return {"success": "Equipamento cadastrado com sucesso."}
        return {"error": "Não foi possível cadastrar o equipamento."}
    
    except Exception as e:
        logger.error("Erro ao cadastrar equipamento: %s", str(e))
        return {"error": "Erro ao cadastrar equipamento."}

# =================== atualizar ===================
def atualizarEquipamento(idEquipamento: int, nome: str, marca: str, quantidade: int, idArea: int) -> dict:
    """ Atualiza os dados de um equipamento existente no banco de dados. """
    try:
        if Equipamentos.atualizar(idArea, nome, marca, quantidade, idEquipamento):
            return {"success": "Equipamento atualizado com sucesso."}
        return {"error": "Falha ao atualizar os dados do equipamento."}
    
    except Exception as e:
        logger.error("Erro ao atualizar equipamento: %s", str(e))
        return {"error": "Erro ao atualizar equipamento."}

# =================== listar ===================
def listarEquipamentos(search_query: str = '') -> dict:
    """ Retorna um dicionário com todos os equipamentos cadastrados, usando o nome como chave e o ID como valor. """
    try:
        todosEquipamentos = Equipamentos.retorna_todos_equipamentos()
        if search_query:
            todosEquipamentos = [eq for eq in todosEquipamentos if search_query.lower() in eq[1].lower()]
        return {eq[1]: eq[0] for eq in todosEquipamentos} if todosEquipamentos else {}
    except Exception as e:
        logger.error("Erro ao listar equipamentos: %s", str(e))
        return {"error": "Erro ao listar equipamentos."}

# =================== remover ===================
def removerEquipamento(idEquipamento: int) -> dict:
    """ Remove um equipamento do banco de dados pelo ID. """
    try:
        if Equipamentos.deletar(idEquipamento):
            return {"success": "Equipamento removido com sucesso."}
        return {"error": "Falha ao remover o equipamento."}
    except Exception as e:
        logger.error("Erro ao remover equipamento: %s", str(e))
        return {"error": "Erro ao remover equipamento."}

# =================== buscar por ID ===================
def buscarEquipamentoId(idEquipamento: int) -> dict:
    """ Busca um equipamento pelo ID e retorna suas informações. """
    if not isinstance(idEquipamento, int):
        return {"error": "ID inválido. Deve ser um número inteiro."}
    try:
        resultado = Equipamentos.pesquisar_id(idEquipamento)
        if not resultado or len(resultado) < 5:
            return {"error": "Equipamento não encontrado."}
        return {
            "idEquipamento": resultado[0],
            "idArea": resultado[1],
            "nome": resultado[2],
            "marca": resultado[3],
            "quantidade": resultado[4]
        }
    except Exception as e:
        logger.error("Erro ao buscar equipamento: %s", str(e))
        return {"error": "Erro ao buscar equipamento."}
