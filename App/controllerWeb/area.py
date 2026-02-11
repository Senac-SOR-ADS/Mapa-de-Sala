from App.model.area import Area
from App.model.logger import logger

# =================== cadastrar ===================
def cadastroDeArea(nomeArea: str) -> dict:
    """ Cadastra uma nova área no banco de dados. """
    try:
        areaModel = Area(nomeArea)
        if areaModel.cadastrar_area():
            return {"success": "Área cadastrada com sucesso."}
        return {"error": "Não foi possível cadastrar a área."}
    
    except Exception as e:
        logger.error("Erro ao cadastrar área: %s", e)
        return {"error": "Erro ao cadastrar área. Consulte os logs para mais detalhes."}

# =================== atualizar ===================
def atualizarArea(idArea: int, nome: str) -> dict:
    """ Atualiza os dados de uma área existente no banco de dados. """
    try:
        if Area.atualizar(idArea, nome):
            return {"success": "Área atualizada com sucesso."}
        return {"error": "Falha ao atualizar os dados da área."}
    
    except Exception as e:
        logger.error("Erro ao atualizar a área. ID: %d, Erro: %s", idArea, e)
        return {"error": "Erro ao atualizar a área. Consulte os logs para mais detalhes."}

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
        logger.error("Erro ao listar áreas. Erro: %s", e)
        return {"error": "Erro ao listar áreas. Consulte os logs para mais detalhes."}

# =================== remover ===================
def removerArea(idArea: int) -> dict:
    """ Remove uma área do banco de dados pelo ID. """
    try:
        result = Area.deletar(idArea)
        
        if result:
            return {"success": "Área removida com sucesso."}
        
        return {"error": "Não foi possível remover a área."}
    
    except Exception as e:
        logger.error("Erro ao remover área. ID: %d, Erro: %s", idArea, e)
        return {"error": "Erro ao remover área. Consulte os logs para mais detalhes."}

# =================== buscar Id ===================
def buscarAreaId(idArea: int) -> dict:
    """Busca uma área pelo ID e retorna suas informações."""
    try:
        resultado = Area.buscar_nome_area(idArea)

        if not resultado:
            return {"error": "Área não encontrada"}

        return {
            "idArea": idArea,
            "nomeArea": resultado,
        }

    except Exception as e:
        logger.error("Erro ao buscar área. ID: %d, Erro: %s", idArea, e)
        return {"error": "Erro ao buscar área. Consulte os logs para mais detalhes."}
