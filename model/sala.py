class Sala:
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