class Equipamentos:
    def __init__(self, nome, marca, quantidade, area) -> None:
        # caracteristicas atributos
        self.__nome = nome
        self.__marca = marca
        self.quantidade = quantidade
        self.__area = area
 
    def get_Nome(self):
        return self.__nome
   
    def nomeset(self, nome):
        self.__nome = nome
 
    def marcaget(self):
        return self.__marca
   
    def nomeset(self, marca):
        self.__marca = marca
 
    def areaget(self):
        return self.__area
   
    def areaset(self, area):
        self.__area = area