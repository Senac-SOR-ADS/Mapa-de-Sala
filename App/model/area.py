from App.model.conexao import ConexaoBD
from App.controller.logger import Log


log = Log('model')

class Area:
    __banco = ConexaoBD()
    
    def __init__(self, nome) -> None:
        self.__nome = nome
 
    def get_nome(self):
        return self.__nome
   
    def set_nome(self, nome):
        self.__nome =  nome

    def cadastrar_area(self):
        """Uma função para fazer o cadastro de uma área"""
        self.__banco.conectar()
        query = "INSERT INTO area (nome) VALUES (%s)"
        parametro = [self.__nome]
        if self.__banco.alterarDados(query, parametro):
            log.info(f'Inserção de área feita com sucesso!, {parametro}')
            self.__banco.desconectar()
            return True
        else:
            log.error(f'{__name__}: Erro ao fazer o cadastro de uma nova área. {parametro}')
            self.__banco.desconectar()
            return False
    
    @classmethod
    def consulta_areas(cls):
        """Uma função que devolve todas as áreas"""
        cls.__banco.conectar()
        query = "SELECT * FROM area"
        resultado = cls.__banco.buscarTodos(query)
        cls.__banco.desconectar()
        return resultado
    
    def consulta_area_curso(self):
        """Uma função que devolve a área junto com os nomes de cursos dessa área"""
        self.__banco.conectar()
        query = "SELECT a.nome, c.nome FROM area a JOIN curso c ON a.idArea = c.idArea"
        resultado = self.__banco.buscarTodos(query)
        self.__banco.desconectar()
        return resultado
    
    def consulta_especifica(self):
        """Uma função que devolve apenas uma área que foi passada"""
        self.__banco.conectar()
        query = "SELECT * FROM area WHERE nome = %s"
        parametro = [self.__nome]
        resultado = self.__banco.buscar(query, parametro)
        self.__banco.desconectar()
        return resultado
    
    def consulta_especifica_curso(self):
        """Uma função que devolve o nome dos cursos da área passada"""
        self.__banco.conectar()
        query = "SELECT a.nome, c.nome FROM area a JOIN curso c ON a.idArea = c.idArea WHERE a.nome = %s"
        parametro = [self.__nome]
        resultado = self.__banco.buscarTodos(query, parametro)
        self.__banco.desconectar()
        return resultado
    
    @classmethod
    def deletar(cls, idArea):
        cls.__banco.conectar()
        query = "DELETE FROM area WHERE idArea = %s"
        parametro = [idArea]
        resultado = cls.__banco.alterarDados(query, parametro)
        cls.__banco.desconectar()
        if resultado.rowcount:
            return True
        return False            
    
    @classmethod
    def atualizar(cls, idArea, nome):
        cls.__banco.conectar()
        query = "UPDATE area SET nome = %s WHERE idArea = %s"
        parametro = [nome, idArea]
        resultado = cls.__banco.alterarDados(query, parametro)
        cls.__banco.desconectar()
        if resultado.rowcount:
            return True
        return False
        

if __name__ == '__main__':
    pass