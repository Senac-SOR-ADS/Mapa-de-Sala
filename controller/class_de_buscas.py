class Login:
    def __init__(self, pessoa, email, senha) -> None:
        self.__pessoa = pessoa
        self.email = email
        self.senha = senha
 
    def Get_pessoa(self):
        return self.__pessoa
   
    def Set_pessoa(self, pessoa):
        self.__pessoa = pessoa
 
 
class Pessoa:
    def __init__(self, nome, cpf_cnpj, nascimento, telefone, email, cargo) -> None:
        self.__nome = nome  
        self.__cpf_cnpj = cpf_cnpj
        self.__nascimento = nascimento
        self.telefone = telefone
        self.email = email
        self.cargo = cargo
 
    def Get_nome(self):
        return self.__nome
   
    def Set_nome(self, nome):
        self.__nome = nome
 
    def Get_cpf_cnpj(self):
        return self.__cpf_cnpj
   
    def Set_cpf_cnpj(self, cpf_cnpj):
        self.__cpf_cnpj = cpf_cnpj
 
    def Get_nascimento(self):
        return self.__nascimento
   
    def Set_nascimento(self, nascimento):
        self.__nascimento = nascimento
   
class area:
    def __init__(self, nome) -> None:
        self.__nome = nome
 
    def Get_nome(self):
        return self.__nome
   
    def Set_nome(self, nome):
        self.__nome =  nome
 
class sala:
    def __init__(self, nome_da_sala, tipo, predio, equipamentos, capacidade, observacao) -> None:
        self.nome_da_sala = nome_da_sala
        self.tipo = tipo
        self.predio = predio
        self.__equipamentos = equipamentos
        self.capacidade = capacidade
        self.observacao = observacao
 
    def Get_equipamentos(self):
        return self.__equipamentos
   
    def  Set_equipamentos(self, equipamentos):
        self.__equipamentos = equipamentos