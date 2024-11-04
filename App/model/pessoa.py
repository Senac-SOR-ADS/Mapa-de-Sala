from App.model.conexao import ConexaoBD
from App.model.criptografia import Criptografia

class Pessoa:
    __banco = ConexaoBD()

    def __init__(self) -> None:
        self.__idPessoa = None
        self.__nome = None
        self.__cpf_cnpj = None
        self.__nascimento = None
        self.__telefone = None
        self.__email = None
        self.__cargo = None

    def get_idPessoa(self):
        return self.__idPessoa
    
    def __set_idPessoa(self, id):
        self.__idPessoa = id

    def get_nome(self):
        return self.__nome
   
    def __set_nome(self, nome):
        self.__nome = nome.title()
 
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

    # Método para cadastrar
    def cadastrar(self, nome, cpf_cnpj, nascimento, telefone, email, cargo):
        self.__set_nome(nome)
        self.__set_cpf_cnpj(cpf_cnpj)
        self.__set_nascimento(nascimento)
        self.__set_telefone(telefone)
        self.__set_email(email)
        self.__set_cargo(cargo)

        try:
            self.__banco.conectar()

            # Inserção na tabela Pessoa
            query_pessoa = '''
            INSERT INTO pessoa (nome, CPF_CNPJ, nascimento, telefone, email, cargo)
            VALUES (%s, %s, %s, %s, %s, %s)
            '''
            params_pessoa = (self.get_nome(), self.get_cpf_cnpj(), self.get_nascimento(), self.get_telefone(), self.get_email(), self.get_cargo())
            resposta = self.__banco.alterarDados(query_pessoa, params_pessoa)
            self.__set_idPessoa(resposta.lastrowid)

            # Inserção na tabela login
            senha_criptografada = Criptografia.criptografarSenha(cpf_cnpj)
            nivelAcesso = 'admin' if cargo == 'Administrador' else 'user'
            query_login = '''
            INSERT INTO login (idPessoa, email, senha, nivelAcesso)
            VALUES (%s, %s, %s, %s)
            '''
            params_login = (self.get_idPessoa(), self.get_email(), senha_criptografada, nivelAcesso)
            self.__banco.alterarDados(query_login, params_login)
            self.__banco.desconectar()
            return True
        except Exception:
            return False

    # Métodos para listar pessoas cadastradas
    @classmethod
    def buscar(cls):
        try:
            cls.__banco.conectar()
            query = 'SELECT idPessoa, nome FROM pessoa;'
            resposta = cls.__banco.buscarTodos(query)
            cls.__banco.desconectar()
            return resposta
        except Exception:
            return False
    
    # Método para buscar por id
    @classmethod
    def pesquisar_id(cls, idPessoa):
        try:
            cls.__banco.conectar()
            query = 'SELECT * FROM pessoa WHERE idPessoa = %s;'
            resposta = cls.__banco.buscar(query, (idPessoa,))
            cls.__banco.desconectar()
            return resposta
        except Exception:
            return False

    # Método para atualizar dados de uma pessoa
    def atualizar(self, idPessoa, nome, cpf_cnpj, nascimento, telefone, email, cargo):
        self.__set_idPessoa(idPessoa)
        self.__set_nome(nome)
        self.__set_cpf_cnpj(cpf_cnpj)
        self.__set_nascimento(nascimento)
        self.__set_telefone(telefone)
        self.__set_email(email)
        self.__set_cargo(cargo)
        try:
            self.__banco.conectar()
            query = '''
                UPDATE pessoa 
                SET nome = %s, CPF_CNPJ = %s, nascimento = %s, telefone = %s, email = %s, cargo = %s 
                WHERE idPessoa = %s
            '''
            params = (self.get_nome(), self.get_cpf_cnpj(), self.get_nascimento(), self.get_telefone(), self.get_email(), self.get_cargo(), self.get_idPessoa())
            self.__banco.alterarDados(query, params)
            self.__banco.desconectar()
            return True
        except Exception:
            return False

    # Método para remover uma pessoa do banco
    @classmethod
    def deletar(cls, idPessoa):
        try:
            cls.__banco.conectar()
            query = 'DELETE FROM pessoa WHERE idPessoa = %s;'
            params = (idPessoa,)
            cls.__banco.alterarDados(query, params)
            cls.__banco.desconectar()
            return True
        except Exception:
            return False
    
if __name__ == "__main__":
    pass
