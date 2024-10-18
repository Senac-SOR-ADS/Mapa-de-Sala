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