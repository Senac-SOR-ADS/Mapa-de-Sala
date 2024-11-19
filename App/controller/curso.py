from App.model.curso import Curso

def cadastrarCurso(area, nome, oferta, periodo, carga, horas, alunos):
    cursoModel = Curso(nome, oferta, periodo, carga, horas, alunos)
    if cursoModel.cadastrar_curso(area):
        return True
    return False

def listarCursos():
    todosCursos = Curso.retorna_nomeId_cursos()
    listaCursos = {i[1]:i[0] for i in todosCursos}
    return listaCursos

def deletarCurso(idCurso):
    if Curso.deletar(idCurso):
        return True
    return False
 
def atualizarCurso(idCurso, idArea, nome, oferta, periodo, cargaHoraria, horasDia, qtdAlunos):
    if Curso.atualizar(idCurso, idArea, nome, oferta, periodo, cargaHoraria, horasDia, qtdAlunos):
        return True
    return False