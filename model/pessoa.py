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
        
        
        
        
    def inserir_pessoa(self):
        self.__banco.conectar()

        query = "INSERT INTO `pessoa`(`nome`, `CPF_CNPJ`, `nascimento`, `telefone`, `email`, `cargo`) VALUES (%s, %s, %s, %s, %s, %s)"
        parametros = (self.__nome, self.__cpf_cnpj, self.__nascimento, self.telefone, self.email, self.cargo)
        resultado = self.__banco(query,  parametros)

        self.__banco.desconectar()


if __name__ == "__main__":
    login = Pessoa('otavio henrique', '879.987.548.32', '2024-10-15', 'otavio@otavio.com', 'Chefe')
    login.inserir_pessoa()
