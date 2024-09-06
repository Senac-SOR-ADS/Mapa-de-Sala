class Login:
    def __init__(self, pessoa, email, senha) -> None:
        self.__pessoa = pessoa
        self.email = email
        self.senha = senha
 
    def get_pessoa(self):
        return self.__pessoa
   
    def set_pessoa(self, pessoa):
        self.__pessoa = pessoa