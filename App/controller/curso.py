from App.model.curso import Curso
from App.controller.utils import validarInputs

# =================== cadastrar ===================
def cadastrarCurso(idArea: int, dados: list) -> dict:
    """Cadastra um novo curso associado a uma área no banco de dados."""
    
    # Validação dos dados de entrada
    if not validarInputs(dados) or not idArea:
        return {"error": "Preencha todos os campos corretamente."}
    
    try:
        # Criação do objeto Curso com os dados fornecidos
        cursoModel = Curso(dados[1], dados[2], dados[3], dados[4], dados[5], dados[6])
        
        # Cadastro do curso no banco de dados
        if cursoModel.cadastrar_curso(idArea):
            return {"success": "Curso cadastrado com sucesso."}
        
        return {"error": "Não foi possível cadastrar o curso."}
    
    except Exception as e:
        return {"error": f"Erro ao cadastrar curso: {e}"}

# =================== listar ===================
def listarCursos(search_query: str = '') -> dict:
    """ Retorna um dicionário com todos os cursos cadastrados, usando o nome como chave e o ID como valor.
    Filtra os resultados com base no nome se a query de pesquisa for fornecida. """
    try:
        todosCursos = Curso.retorna_nomeId_cursos()

        if search_query:
            todosCursos = [curso for curso in todosCursos if search_query.lower() in curso[1].lower()]

        return {curso[1]: curso[0] for curso in todosCursos} if todosCursos else {}
    except Exception as e:
        return {"error": f"Erro ao listar cursos: {e}"}

# =================== atualizar ===================
def atualizarCurso(idCurso: int, idArea: int, nome: str, oferta: str, periodo: str, cargaHoraria: int, horasDia: int, qtdAlunos: int) -> dict:
    """ Atualiza os dados de um curso existente no banco de dados. """
    try:
        if Curso.atualizar(idCurso, idArea, nome, oferta, periodo, cargaHoraria, horasDia, qtdAlunos):
            return {"success": "Curso atualizado com sucesso."}
        return {"error": "Não foi possível atualizar o curso."}
    except Exception as e:
        return {"error": f"Erro ao atualizar curso: {e}"}

# =================== remover ===================
def removerCurso(idCurso: int) -> dict:
    """ Remove um curso do banco de dados pelo ID. """
    try:
        if Curso.deletar(idCurso):
            return {"success": "Curso removido com sucesso."}
        return {"error": "Não foi possível remover o curso."}
    except Exception as e:
        return {"error": f"Erro ao remover curso: {e}"}

# =================== buscar Id ===================
def buscarCursoId(idCurso: int) -> dict:
    """ Busca um curso pelo ID e retorna suas informações ou uma mensagem de erro se não for encontrado. """
    if not isinstance(idCurso, int):
        return {"error": "ID inválido. Deve ser um número inteiro."}

    try:
        resultado = Curso.retorna_curso_id(idCurso)

        if not resultado or len(resultado) < 8:
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
        return {"error": f"Erro ao buscar curso: {e}"}
