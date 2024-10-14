from App.model.curso import Curso

def cadastrarCurso(area, nome, oferta, periodo, carga, horas, alunos):
    cursoModel = Curso(nome, oferta, periodo, carga, horas, alunos)
    if cursoModel.cadastrar_curso(area):
        return True
    return False

