from conexao import ConexaoBD


class Sala:
    __banco = ConexaoBD()

    def __init__(self, nome_da_sala, tipo, predio, equipamentos, capacidade, observacao) -> None:
        self.nome_da_sala = nome_da_sala
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
    def cadastrar_sala(cls):
        cls.__banco.conectar()
        query = '''INSERT INTO `sala`(`nome_da_sala`, `tipo`, `predio`, `equipamentos`, `capacidade`, `observacao`) VALUES (%s, %s, %s, %s, %s, %s); '''
        parametros = (cls.nome_da_sala, cls.tipo, cls.predio, cls.__equipamentos, cls.capacidade, cls.observacao)
        resultado = cls.__banco.commit(query, parametros)
        cls.__banco.desconectar()
        return resultado
    
if __name__ == "__main__":
    sala = Sala.cadastrar_sala()
    print(sala)


if __name__ == "__main__":
    teste_buscar_sala = Sala.buscar_sala()
    print(teste_buscar_sala)


if __name__ == "__main__":
    buscar_sala_predio1 = Sala.buscar_sala_predio1()
    print(buscar_sala_predio1)


if __name__ == "__main__":
    buscar_sala_predio2 = Sala.buscar_sala_predio2()
    print(buscar_sala_predio2)
    
