from App.model.curso import Curso
from App.controller.utils import validarInputs

def cadastrarCurso(idArea, dados):
    if validarInputs(dados) and idArea:
        cursoModel = Curso(dados[1], dados[2], dados[3], dados[4], dados[5], dados[6])
        if cursoModel.cadastrar_curso(idArea):
            return True
    print('Preencha todos os campos')
    return False

def listarCursos():
    todosCursos = Curso.retorna_nomeId_cursos()
    listaCursos = {i[1]:i[0] for i in todosCursos}
    return listaCursos

def deletarCurso(idCurso):
    if Curso.deletar(idCurso):
        return True
    return False

def buscarCursoId(idCurso):
    if not isinstance(idCurso, int):
        print('Coloque um id como númerico')
    try:
        resultado = Curso.retorna_curso_id(idCurso)

        if resultado:
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
        return {"erro": "Curso não encontrado"}
    except Exception as e:
        return {"erro": f"Erro ao buscar curso: {e}"}
 
def atualizarCurso(idCurso, idArea, nome, oferta, periodo, cargaHoraria, horasDia, qtdAlunos):
    if Curso.atualizar(idCurso, idArea, nome, oferta, periodo, cargaHoraria, horasDia, qtdAlunos):
        return True
    return False
