from App.model.equipamentos import Equipamentos
from App.controller.utils import validarInputs

# =================== cadastrar ===================
def cadastrarEquipamento(nome: str, marca: str, quantidade: int, id_area: int) -> dict:
    """ Cadastra um novo equipamento no banco de dados. """

    # Validação dos dados de entrada
    if not validarInputs([nome, marca, quantidade, id_area]):
        return {"error": "Preencha todos os campos corretamente."}
    
    try:
        # Cadastro do equipamento no banco de dados
        equipamento = Equipamentos(nome, marca, quantidade, id_area)
        id_equipamento = equipamento.cadastrar_equipamento(id_area)
        
        if id_equipamento:
            return {"success": "Equipamento cadastrado com sucesso.", "idEquipamento": id_equipamento}
        
        return {"error": "Não foi possível cadastrar o equipamento."}
    
    except Exception as e:
        return {"error": f"Erro ao cadastrar equipamento: {str(e)}"}

# =================== atualizar ===================
def atualizarEquipamento(idEquipamento: int, nome: str, marca: str, quantidade: int, id_area: int) -> dict:
    """ Atualiza os dados de um equipamento existente no banco de dados. """
    try:
        equipamentoModel = Equipamentos(nome, marca, quantidade, id_area)
        if equipamentoModel.atualizar(id_area, nome, marca, quantidade, idEquipamento):
            return {"success": "Equipamento atualizado com sucesso."}
        return {"error": "Falha ao atualizar os dados do equipamento."}
    
    except Exception as e:
        return {"error": f"Erro ao atualizar equipamento: {str(e)}"}

# =================== listar ===================
def listarEquipamentos(search_query: str = '') -> dict:
    """ Retorna um dicionário com todos os equipamentos cadastrados.
    Filtra os resultados com base no nome ou marca se a query de pesquisa for fornecida. """
    try:
        todosEquipamentos = Equipamentos.retorna_todos_equipamentos()

        if search_query:
            todosEquipamentos = [
                eq for eq in todosEquipamentos if search_query.lower() in eq[0].lower()
            ]
        
        return {f"{eq[0]}": eq[0] for eq in todosEquipamentos} if todosEquipamentos else {}
    except Exception as e:
        return {"error": f"Erro ao listar equipamentos: {str(e)}"}

# =================== remover ===================
def removerEquipamento(idEquipamento: int) -> dict:
    """ Remove um equipamento do banco de dados pelo ID. """
    try:
        if Equipamentos.deletar(idEquipamento):
            return {"success": "Equipamento removido com sucesso."}
        return {"error": "Falha ao remover o equipamento."}
    except Exception as e:
        return {"error": f"Erro ao remover equipamento: {str(e)}"}

# =================== buscar por ID ===================
def buscarEquipamentoId(idEquipamento: int) -> dict:
    """ Busca um equipamento pelo ID e retorna suas informações ou uma mensagem de erro se não for encontrado. """
    if not isinstance(idEquipamento, int):
        return {"error": "ID inválido. Deve ser um número inteiro."}

    try:
        resultado = Equipamentos.pesquisar_id(idEquipamento)

        if not resultado or len(resultado) < 5:
            return {"error": "Equipamento não encontrado"}

        return {
            "idEquipamento": resultado[0],
            "nome": resultado[1],
            "marca": resultado[2],
            "quantidade": resultado[3],
            "id_area": resultado[4],
        }
    except Exception as e:
        return {"error": f"Erro ao buscar equipamento: {str(e)}"}
