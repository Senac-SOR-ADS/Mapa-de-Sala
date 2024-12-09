from App.model.area import Area
from App.controller.utils import validarInputs

# =================== cadastrar ===================
def cadastroDeArea(nomeArea: str) -> dict:
    """ Cadastra uma nova área no banco de dados. """
    
    # Validar dados de entrada
    if not validarInputs([nomeArea]):
        return {"error": "Preencha todos os campos corretamente."}
    
    try:
        # Criação do objeto Area e cadastro no banco de dados
        areaModel = Area(nomeArea)
        if areaModel.cadastrar_area():
            return {"success": "Área cadastrada com sucesso."}
        return {"error": "Não foi possível cadastrar a área."}
    
    except Exception as e:
        return {"error": f"Erro ao cadastrar área: {e}"}

# =================== atualizar ===================
def atualizarArea(idArea: int, nome: str) -> dict:
    """ Atualiza os dados de uma área existente no banco de dados. """
    try:
        if Area.atualizar(idArea, nome):
            return {"success": "Área atualizada com sucesso."}
        return {"error": "Falha ao atualizar os dados da área."}
    
    except Exception as e:
        return {"error": f"Erro ao atualizar a área: {e}"}

# =================== listar ===================
def listarAreas(search_query: str = '') -> dict:
    """ Retorna um dicionário com as áreas cadastradas, usando o nome como chave e o ID como valor. 
        Search_query filtra pelo nome se fornecido. """
    try:
        todasAreas = Area.consulta_areas()

        if search_query:
            todasAreas = [a for a in todasAreas if search_query.lower() in a[1].lower()]

        return {a[1]: a[0] for a in todasAreas} if todasAreas else {}
    
    except Exception as e:
        return {"error": f"Erro ao listar áreas: {str(e)}"}

# =================== buscar Id ===================
def buscarAreaId(idArea: int) -> dict:
    """ Busca uma área pelo ID e retorna suas informações ou uma mensagem de erro se não for encontrada. """
    if not isinstance(idArea, int):
        return {"error": "ID inválido. Deve ser um número inteiro."}
    
    try:
        resultado = Area.consultar_id(idArea)
        
        if not resultado or len(resultado) < 2:
            return {"error": "Área não encontrada"}
        
        return {
            "idArea": resultado[0],
            "nomeArea": resultado[1],
        }
    
    except Exception as e:
        return {"error": f"Erro ao buscar área: {e}"}

# =================== remover ===================
def removerArea(idArea: int) -> dict:
    """ Remove uma área do banco de dados pelo ID. """
    try:
        result = Area.deletar(idArea)
        
        if result:
            return {"success": "Área removida com sucesso."}
        
        return {"error": "Não foi possível remover a área."}
    
    except Exception as e:
        return {"error": f"Erro ao remover área: {e}"}
