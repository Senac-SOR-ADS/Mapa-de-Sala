from App.model.conexao import ConexaoBD


class Sala:
    __banco = ConexaoBD()

    def __init__(self, nome, tipo, predio, equipamentos, capacidade, observacao) -> None:
        self.nome = nome
        self.tipo = tipo
        self.predio = predio
        self.__equipamentos = equipamentos
        self.capacidade = capacidade
        self.observacao = observacao
        
 
    def get_equipamentos(self):
        return self.__equipamentos
   
    def  set_equipamentos(self, equipamentos):
        self.__equipamentos = equipamentos

    @classmethod
    def buscar_sala(cls):
        cls.__banco.conectar()
        query = '''SELECT * FROM sala;'''
        resultado = cls.__banco.buscarTodos(query)
        cls.__banco.desconectar()
        return resultado
    
    @classmethod
    def buscar_sala_predio1(cls):
        cls.__banco.conectar()  
        query = ''' SELECT * FROM `sala` WHERE predio = 1; '''
        resultado = cls.__banco.buscarTodos(query)
        cls.__banco.desconectar()
        return resultado
    
    @classmethod
    def buscar_sala_predio2(cls):
        cls.__banco.conectar()
        query = '''SELECT * FROM `sala` WHERE predio = 2;'''
        resultado = cls.__banco.buscarTodos(query)
        cls.__banco.desconectar
        return resultado
    
    @classmethod
    def buscar_nomeId_sala(cls):
        cls.__banco.conectar()
        query = '''SELECT idSala, nome FROM `sala`; '''
        resultado = cls.__banco.buscarTodos(query)
        cls.__banco.desconectar
        return resultado
    


    def cadastrar_sala(self):
        self.__banco.conectar()
        query = '''INSERT INTO `sala`(`nome`, `tipo`, `predio`, `equipamentos`, `capacidade`, `observacao`) VALUES (%s, %s, %s, %s, %s, %s); '''
        parametros = (self.nome, self.tipo, self.predio, self.__equipamentos, self.capacidade, self.observacao)
        resultado = self.__banco.alterarDados(query, parametros)
        self.__banco.desconectar()
        return resultado
    
    @classmethod
    def deletar(cls, idSala):
        cls.__banco.conectar()
        query = "DELETE FROM sala WHERE idSala = %s"
        parametro = [idSala]
        resultado = cls.__banco.alterarDados(query, parametro)
        cls.__banco.desconectar()
        if resultado.rowcount:
            return True
        return False
    
    @classmethod
    def atualizar(cls, nome, tipo, predio, equipamento, capacidade, observacao, idSala):
        cls.__banco.conectar()
        query = "UPDATE sala SET `nome`= %s,`tipo`= %s,`predio`= %s,`equipamentos`= %s,`capacidade`= %s,`observacao`= %s WHERE idSala = %s"
        parametro = [nome, tipo, predio, equipamento, capacidade, observacao, idSala]
        resultado = cls.__banco.alterarDados(query, parametro)
        cls.__banco.desconectar()
        if resultado.rowcount:
            return True
        return False
    
   
if __name__ == "__main__":
    pass