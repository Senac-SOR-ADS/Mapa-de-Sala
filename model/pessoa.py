from conexao import ConexaoBD


class Pessoa:
    def __init__(self, nome, cpf_cnpj, nascimento, telefone, email, cargo) -> None:
        self.__nome = nome  
        self.__cpf_cnpj = cpf_cnpj
        self.__nascimento = nascimento
        self.telefone = telefone
        self.email = email
        self.cargo = cargo
        self.__banco = ConexaoBD()
 
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