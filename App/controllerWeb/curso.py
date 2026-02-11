from App.model.curso import Curso
from App.model.logger import logger

# =================== cadastrar ===================
def cadastrarCurso(idArea: int, dados: list) -> dict:
    """Cadastra um novo curso associado a uma área no banco de dados."""
    if not idArea:
        logger.error("ID da área é obrigatório.")
        return {"error": "ID da área é obrigatório."}
    
    try:
        cursoModel = Curso(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5])
        
        if cursoModel.cadastrar_curso(idArea):
            logger.info("Curso cadastrado com sucesso.")
            return {"success": "Curso cadastrado com sucesso."}
        
        logger.error("Não foi possível cadastrar o curso.")
        return {"error": "Não foi possível cadastrar o curso."}
    
    except Exception as e:
        logger.error("Erro ao cadastrar curso: %s", e)
        return {"error": f"Erro ao cadastrar curso: {e}"}

# =================== atualizar ===================
def atualizarCurso(idCurso: int, idArea: int, nome: str, oferta: str, periodo: str, cargaHoraria: int, horasDia: int, qtdAlunos: int) -> dict:
    """ Atualiza os dados de um curso existente no banco de dados. """
    try:
        if Curso.atualizar(idCurso, idArea, nome, oferta, periodo, cargaHoraria, horasDia, qtdAlunos):
            logger.info("Curso atualizado com sucesso. ID do curso: %s", idCurso)
            return {"success": "Curso atualizado com sucesso."}
        logger.error("Não foi possível atualizar o curso. ID do curso: %s", idCurso)
        return {"error": "Não foi possível atualizar o curso."}
    except Exception as e:
        logger.error("Erro ao atualizar curso (ID: %s): %s", idCurso, e)
        return {"error": f"Erro ao atualizar curso: {e}"}

# =================== listar ===================
def listarCursos(search_query: str = '') -> dict:
    """ Retorna um dicionário com todos os cursos cadastrados, usando o nome como chave e o ID como valor.
    Filtra os resultados com base no nome se a query de pesquisa for fornecida. """
    try:
        todosCursos = Curso.retorna_todos_nomes_cursos()

        if search_query:
            todosCursos = [curso for curso in todosCursos if search_query.lower() in curso[1].lower()]

        return {curso[1]: curso[0] for curso in todosCursos} if todosCursos else {}
    except Exception as e:
        logger.error("Erro ao listar cursos: %s", e)
        return {"error": f"Erro ao listar cursos: {e}"}
    
# =================== remover ===================
def removerCurso(idCurso: int) -> dict:
    """ Remove um curso do banco de dados pelo ID. """
    try:
        if Curso.deletar(idCurso):
            logger.info("Curso removido com sucesso. ID do curso: %s", idCurso)
            return {"success": "Curso removido com sucesso."}
        logger.error("Não foi possível remover o curso. ID do curso: %s", idCurso)
        return {"error": "Não foi possível remover o curso."}
    except Exception as e:
        logger.error("Erro ao remover curso (ID: %s): %s", idCurso, e)
        return {"error": f"Erro ao remover curso: {e}"}

# =================== buscar Id ===================
def buscarCursoId(idCurso: int) -> dict:
    """ Busca um curso pelo ID e retorna suas informações ou uma mensagem de erro se não for encontrado. """
    if not isinstance(idCurso, int):
        logger.error("ID inválido. Deve ser um número inteiro.")
        return {"error": "ID inválido. Deve ser um número inteiro."}

    try:
        resultado = Curso.pesquisar_id(idCurso)

        if not resultado:
            logger.error("Curso não encontrado. ID do curso: %s", idCurso)
            return {"error": "Curso não encontrado."}

        return {
            "idCurso": resultado[0],
            "idArea": resultado[1],
            "nome": resultado[2],
            "oferta": resultado[3],
            "periodo": resultado[4],
            "cargaHoraria": resultado[5],
            "horasDia": resultado[6],
            "qtdAlunos": resultado[7],
        }
    except Exception as e:
        logger.error("Erro ao buscar curso (ID: %s): %s", idCurso, e)
        return {"error": f"Erro ao buscar curso: {e}"}
