from conexao import ConexaoBD


class Equipamentos:
    __banco = ConexaoBD()
    
    def __init__(self, nome, marca, quantidade, area) -> None:
        # caracteristicas atributos 
        self.__nome = nome
        self.__marca = marca
        self.quantidade = quantidade
        self.__area = area
        self.__idArea = None
 
    def get_nome(self):
        return self.__nome
   
    def set_nome(self, nome):
        self.__nome = nome
 
    def get_marca(self):
        return self.__marca
   
    def set_nome(self, marca):
        self.__marca = marca
 
    def get_area(self):
        return self.__area
   
    def set_area(self, area):
        self.__area = area
        

    def cadastrar_equipamento(self, id_area):
        self.__banco.conectar()
        query = "INSERT INTO `equipamento`(`idArea`, `nome`, `marca`, `quantidade`) VALUES (%s, %s, %s, %s)"
        params = [id_area, self.__nome, self.__marca, self.quantidade]
        resultado = self.__banco.alterarDados(query, params)
        self.__banco.desconectar()
        return resultado
    
    
    @classmethod
    def retorna_equipamento_reservado(cls):
        cls.__banco.conectar()
        query = "SELECT e.nome FROM equipamento e RIGHT JOIN ocupado o ON o.idEquipamento = e.idEquipamento"
        resultado = cls.__banco.buscarTodos(query)
        cls.__banco.desconectar()
        return resultado
    
    @classmethod
    def retorna_equipamentos_sem_reserva(cls):
        cls.__banco.conectar()
        query ="SELECT e.nome FROM ocupado o RIGHT JOIN equipamento e ON o.idEquipamento = e.idEquipamento WHERE o.idEquipamento IS NULL;"
        resultado = cls.__banco.buscarTodos(query)
        cls.__banco.desconectar()
        return resultado
    
    @classmethod
    def retorna_todos_equipamentos(cls):
        cls.__banco.conectar()
        query = "SELECT nome FROM equipamento"
        resultado = cls.__banco.buscarTodos(query)
        cls.__banco.desconectar()
        return resultado
    
    @classmethod
    def retorna_sala_equipamento(cls):
        cls.__banco.conectar()
        query = "SELECT e.nome AS nomeEquipamento, e.marca, r.idSala, s.nome AS nomeSala FROM equipamento e INNER JOIN ocupado o ON e.idEquipamento = o.idEquipamento INNER JOIN reserva r ON o.idReserva = r.idReserva INNER JOIN sala s ON r.idSala = s.idSala "
        resultado = cls.__banco.buscarTodos(query)
        cls.__banco.desconectar()
        return resultado
    
    
    @classmethod
    def retorna_nome_quantidade_sala_docente_equipamento(cls):
        cls.__banco.conectar()
        query = "SELECT e.nome AS nomeEquipamento, r.idPessoa, r.idSala, p.nome AS nomePessoa, s.nome AS nomeSala FROM equipamento e INNER JOIN ocupado o ON e.idEquipamento = o.idEquipamento INNER JOIN reserva r ON o.idReserva = r.idReserva INNER JOIN sala s ON r.idSala = s.idSala INNER JOIN pessoa p ON r.idPessoa = p.idPessoa"
        resultado =cls.__banco.buscarTodos(query)
        cls.__banco.desconectar()
        return resultado
    
    
 
    
    
if __name__ == "__main__":
    teste = Equipamentos('Monitor', 'Dell', 10, 'Tecnologia da Informação')
    res = teste.cadastrar_equipamento(1)
    print(res)