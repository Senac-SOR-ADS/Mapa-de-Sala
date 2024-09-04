class Login:
    def __init__(self, pessoa, email, senha) -> None:
        self.__pessoa = pessoa
        self.email = email
        self.senha = senha
 
    def get_pessoa(self):
        return self.__pessoa
   
    def set_pessoa(self, pessoa):
        self.__pessoa = pessoa
 
 
class Pessoa:
    def __init__(self, nome, cpf_cnpj, nascimento, telefone, email, cargo) -> None:
        self.__nome = nome  
        self.__cpf_cnpj = cpf_cnpj
        self.__nascimento = nascimento
        self.telefone = telefone
        self.email = email
        self.cargo = cargo
 
    def get_nome(self):
        return self.__nome
   
    def set_nome(self, nome):
        self.__nome = nome
 
    def get_cpf_cnpj(self):
        return self.__cpf_cnpj
   
    def set_cpf_cnpj(self, cpf_cnpj):
        self.__cpf_cnpj = cpf_cnpj
 
    def get_nascimento(self):
        return self.__nascimento
   
    def set_nascimento(self, nascimento):
        self.__nascimento = nascimento
   
class Area:
    def __init__(self, nome) -> None:
        self.__nome = nome
 
    def get_nome(self):
        return self.__nome
   
    def set_nome(self, nome):
        self.__nome =  nome