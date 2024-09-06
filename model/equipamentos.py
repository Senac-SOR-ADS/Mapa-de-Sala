class Equipamentos:
    def __init__(self, nome, marca, quantidade, area) -> None:
        # caracteristicas atributos
        self.__nome = nome
        self.__marca = marca
        self.quantidade = quantidade
        self.__area = area
 
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