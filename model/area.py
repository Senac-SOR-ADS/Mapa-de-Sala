class Area:
    def __init__(self, nome) -> None:
        self.__nome = nome
 
    def get_nome(self):
        return self.__nome
   
    def set_nome(self, nome):
        self.__nome =  nome