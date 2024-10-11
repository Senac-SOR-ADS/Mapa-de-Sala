from App.model.conexao import ConexaoBD


class Area:
    def __init__(self, nome) -> None:
        self.__nome = nome
        self.__banco = ConexaoBD()
 
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
            self.__banco.desconectar()
            return True
        else:
            self.__banco.desconectar()
            return False
    
    def consulta_areas(self):
        """Uma função que devolve todas as áreas"""
        self.__banco.conectar()
        query = "SELECT * FROM area"
        resultado = self.__banco.buscarTodos(query)
        self.__banco.desconectar()
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
    
    def consulta_nome_areas(self):
        self.__banco.conectar()
        query = 'SELECT nome FROM area'
        resultado = self.__banco.buscarTodos(query)
        self.__banco.desconectar()
        return resultado

if __name__ == '__main__':
    pass