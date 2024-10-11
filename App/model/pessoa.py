from App.model.conexao import ConexaoBD


class Pessoa:

    def __init__(self) -> None:

        self.__idPessoa = None
        self.__nome = None
        self.__cpf_cnpj = None
        self.__nascimento = None
        self.telefone = None
        self.email = None
        self.cargo = None
        self.__banco = ConexaoBD()

    def get_idPessoa(self):
        return self.__idPessoa
    
    def __set_idPessoa(self, id):
        self.__idPessoa = id

    def get_nome(self):
        return self.__nome
   
    def __set_nome(self, nome):
        self.__nome = nome
 
    def get_cpf_cnpj(self):
        return self.__cpf_cnpj
   
    def __set_cpf_cnpj(self, cpf_cnpj):
        self.__cpf_cnpj = cpf_cnpj
 
    def get_nascimento(self):
        return self.__nascimento
   
    def __set_nascimento(self, nascimento):
        self.__nascimento = nascimento

    def get_telefone(self):
        return self.__telefone
   
    def __set_telefone(self, telefone):
        self.__telefone = telefone

    def get_email(self):
        return self.__email
   
    def __set_email(self, email):
        self.__email = email

    def get_cargo(self):
        return self.__cargo
   
    def __set_cargo(self, cargo):
        self.__cargo = cargo

    def cadastrar(self, nome, cpf_cnpj, nascimento, telefone, email, cargo):

        self.__set_nome(nome)
        self.__set_cpf_cnpj(cpf_cnpj)
        self.__set_nascimento(nascimento)
        self.__set_telefone(telefone)
        self.__set_email(email)
        self.__set_cargo(cargo)

        try:
            self.__banco.conectar()

            query = 'INSERT INTO pessoa (`nome`, `CPF_CNPJ`, `nascimento`, `telefone`, `email`, `cargo`) VALUES (%s, %s, %s, %s, %s, %s)'
            params = (nome, cpf_cnpj, nascimento, telefone, email, cargo)
            resposta = self.__banco.alterarDados(query, params)
            self.__set_idPessoa(resposta.lastrowid)
            self.__banco.desconectar()
            return True
        
        except Exception as e:
            return False

if __name__ == "__main__":

    p = Pessoa()
    p.cadastrar('Jeff', '123.456.789-00', '2006-10-19', '(15) 99120-6869', 'jeff@gmail.com', 'Gerente Master')
    # p.__set_nome('mario') # não pode acontece

    print(p)
    print(p.get_nome())
    print(p.get_cpf_cnpj())
    print(p.get_idPessoa())
    
    # print(p.get_id)


