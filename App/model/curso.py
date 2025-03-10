from App.model.conexao import ConexaoBD
from App.controller.logger import Log

log = Log('model')


class Curso:
    __banco = ConexaoBD()
 
    def __init__(self, nome, oferta, periodo, cargaHoraria, horasDia, qtdAlunos):
        self.__nome = nome
        self.__oferta = oferta
        self.__periodo = periodo
        self.__cargaHoraria = cargaHoraria
        self.__horasDia = horasDia
        self.__qtdAlunos = qtdAlunos
        self.__id = None

    def __set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
 
    def set_nome(self, nome):
        self.__nome = nome
 
    def get_oferta(self):
        return self.__oferta
 
    def set_oferta(self, oferta):
        self.__oferta = oferta
 
    def get_periodo(self):
        return self.__periodo
 
    def set_periodo(self, periodo):
        self.__periodo = periodo
 
    def get_cargaHoraria(self):
        return self.__cargaHoraria
 
    def set_cargaHoraria(self, cargaHoraria):
        self.__cargaHoraria = cargaHoraria
 
    def get_horasDia(self):
        return self.__horasDia
 
    def set_horasDia(self, horasDia):
        self.__horasDia = horasDia
 
    def get_qtdAlunos(self):
        return self.__qtdAlunos
 
    def set_qtdAlunos(self, qtdAlunos):
        self.__qtdAlunos = qtdAlunos
 
    def cadastrar_curso(self, id_area):
        self.__banco.conectar()
        query = "INSERT INTO `curso`(`idArea`, `nome`, `oferta`, `periodo`, `cargaHoraria`, `horasDia`, `qtdAlunos`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        params = [id_area, self.__nome, self.__oferta, self.__periodo, self.__cargaHoraria, self.__horasDia, self.__qtdAlunos]
        resultado = self.__banco.alterarDados(query, params)
        self.__banco.desconectar()
        if resultado:
            return True
        return False
    
    ######## JEFF
    @classmethod
    def retorna_info_cursos(cls)->list:
        cls.__banco.conectar()
        query = "SELECT * FROM curso"
        resultado = cls.__banco.buscarTodos(query)
        cls.__banco.desconectar()
        lista_cursos = list()
        for item in resultado:
            curso = cls(item[2], item[3], item[4], item[5], item[6], item[7])
            curso.__set_id(item[0])
            lista_cursos.append(curso)
        return lista_cursos
    ########
 
    @classmethod
    def retorna_todos_cursos(cls):
        cls.__banco.conectar()
        query = "SELECT nome FROM curso"
        resultado = cls.__banco.buscarTodos(query)
        cls.__banco.desconectar()
        return resultado
 
    @classmethod
    def retorna_curso_area(cls, id_area):
        cls.__banco.conectar()
        query = "SELECT * FROM curso WHERE idArea = %s"
        params = [id_area]
        resultado = cls.__banco.buscarTodos(query, params)
        cls.__banco.desconectar()
        return resultado
 
    @classmethod
    def retorna_curso_periodo(cls, periodo):
        cls.__banco.conectar()
        query = "SELECT * FROM curso WHERE periodo = %s"
        params = [periodo]
        resultado = cls.__banco.buscarTodos(query, params)
        cls.__banco.desconectar()
        return resultado
    
    @classmethod
    def retorna_ofertaId_cursos(cls):
        cls.__banco.conectar()
        query = "SELECT idCurso, oferta FROM curso"
        resultado = cls.__banco.buscarTodos(query)
        cls.__banco.desconectar()
        return resultado
    
    @classmethod
    def retorna_todas_infos_curso(cls, idCurso):
        cls.__banco.conectar()
        query = "SELECT * FROM curso WHERE idCurso = %s"
        param = [idCurso]
        resultado = cls.__banco.buscar(query, param)
        cls.__banco.desconectar()
        return resultado


    @classmethod
    def deletar(cls, idCurso):
        cls.__banco.conectar()
        query = "DELETE FROM curso WHERE idCurso = %s"
        param = [idCurso]
        resultado = cls.__banco.alterarDados(query, param)
        cls.__banco.desconectar()
        if resultado.rowcount:
            log.info('curso deletado')
            return True
        log.error('erro ao deletar curso.')
        return False
    
    @classmethod
    def atualizar(cls, idCurso, idArea, nome, oferta, periodo, cargaHoraria, horasDia, qtdAlunos):
        cls.__banco.conectar()
        query = "UPDATE curso SET idArea = %s, nome = %s, oferta = %s, periodo = %s, cargaHoraria = %s, horasDia = %s, qtdAlunos = %s WHERE idCurso = %s"
        params = [idArea, nome, oferta, periodo, cargaHoraria, horasDia, qtdAlunos, idCurso]
        resultado = cls.__banco.alterarDados(query, params)
        cls.__banco.desconectar()
        if resultado.rowcount:
            return True
        return False
    


#  EXEMPLO PESQUISA AREA
if __name__ == "__main__":
    teste = Curso.retorna_curso_area(1)  # Passando um exemplo de AREA
    print(teste)

#  EXEMPLO PESQUISA PERIODO
if __name__ == "__main__":
    teste = Curso.retorna_curso_periodo('Tarde')  # Passando um exemplo de PERIODO
    print(teste)
 