from App.model.conexao import ConexaoBD
from App.model.criptografia import Criptografia

class Login:
    def __init__(self, email=None, senha=None) -> None:
        self.__email = email
        self.__senha = senha
        self.__idLogin = None
        self.__idPessoa = None
        self.__banco = ConexaoBD()

    def getIdLogin(self):
        return self.__idLogin

    def setIdLogin(self, id):
        self.__idLogin = id

    def getIdPessoa(self):
        return self.__idPessoa

    def setIdPessoa(self, id):
        self.__idPessoa = id

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getSenha(self):
        return self.__senha

    def setSenha(self, senha):
        self.__senha = senha

    def cadastrar(self, idPessoa, cpf_cnpj, email, cargo):
        # Definir atributos do usuário
        self.setIdPessoa(idPessoa)
        self.setEmail(email)
        self.setSenha(cpf_cnpj)

        # Criptografar senha usando cpf_cnpj
        senha_criptografada = Criptografia.criptografarSenha(cpf_cnpj)

        # Definir nível de acesso com base no cargo
        nivelAcesso = 'admin' if cargo == 'Administrador' else 'user'

        try:
            # Conectar ao banco de dados
            self.__banco.conectar()

            # Preparar e executar a inserção no banco de dados
            query_login = '''
            INSERT INTO login (idPessoa, email, senha, nivelAcesso)
            VALUES (%s, %s, %s, %s)
            '''
            params_login = (self.getIdPessoa(), self.getEmail(), senha_criptografada, nivelAcesso)
            self.__banco.alterarDados(query_login, params_login)
            return True

        except Exception as e:
            print(f"Erro ao cadastrar login: {e}")
            return False
        finally:
            self.__banco.desconectar()

    def validarLogin(self):
        self.__banco.conectar()

        query = "SELECT * FROM login WHERE email = %s;"
        parametro = [self.getEmail()]
        resultado = self.__banco.buscar(query, parametro)

        self.__banco.desconectar()

        try:
            senhaBanco = resultado[3]
            senhaBanco = senhaBanco.encode('utf-8')
            senhaUsuario = self.getSenha()

            if self.getEmail() == resultado[2] and Criptografia.validarSenha(senhaUsuario, senhaBanco):
                self.setIdLogin(resultado[0])
                self.setIdPessoa(resultado[1])
                return True
        except Exception as e:
            print(f"Erro na validação de login: {e}")
            return False

if __name__ == "__main__":
    pass