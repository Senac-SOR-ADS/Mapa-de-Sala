from App.model.conexao import ConexaoBD
from App.model.criptografia import Criptografia

class Login:
    def __init__(self, email=None, senha=None, nivel_acesso='user') -> None:
        self.__email = email
        self.__senha = senha
        self.__idLogin = None
        self.__idPessoa = None
        self.__nivelAcesso = nivel_acesso
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

    def getNivelAcesso(self):
        return self.__nivelAcesso

    def setNivelAcesso(self, nivel_acesso):
        self.__nivelAcesso = nivel_acesso

    # =================== cadastrar ===================
    def cadastrar(self, idPessoa, cpf_cnpj, email, cargo):
        self.setIdPessoa(idPessoa)
        self.setEmail(email)
        self.setSenha(cpf_cnpj)

        senha_criptografada = Criptografia.criptografarSenha(cpf_cnpj)
        nivelAcesso = 'admin' if cargo == 'Administrador' else 'user'

        try:
            self.__banco.conectar()

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

    # =================== atualizar ===================
    def atualizar(self, idLogin, email, cargo):
        """Atualiza o email e o nível de acesso do usuário no banco de dados."""
        
        nivelAcesso = 'admin' if cargo == 'Administrador' else 'user'
        try:
            self.__banco.conectar()

            query_update = '''
                UPDATE login
                SET email = %s, nivelAcesso = %s
                WHERE idLogin = %s
            '''
            self.__banco.alterarDados(query_update, (email, nivelAcesso, idLogin))
            return True
        except Exception as e:
            print(f"Erro ao atualizar login: {e}")
            return False
        finally:
            self.__banco.desconectar()

    # =================== listar ===================
    def buscar(self, idLogin):
        self.__banco.conectar()

        query = "SELECT * FROM login WHERE idLogin = %s;"
        parametro = (idLogin,)
        resultado = self.__banco.buscar(query, parametro)
        self.__banco.desconectar()

        if resultado:
            self.setIdLogin(resultado[0])
            self.setIdPessoa(resultado[1])
            self.setEmail(resultado[2])
            self.setSenha(resultado[3])
            self.setNivelAcesso(resultado[4])
            return True
        return False
    
    # =================== buscar por Id ===================
    @classmethod
    def pesquisar_id(cls, idLogin):
        try:
            cls.__banco.conectar()
            query = 'SELECT * FROM login WHERE idLogin = %s;'
            resposta = cls.__banco.buscar(query, (idLogin,))
            cls.__banco.desconectar()
            return resposta if resposta else False
        except Exception as e:
            print(f"Erro ao pesquisar login: {e}")
            return False

    # =================== Remove ===================
    @classmethod
    def deletar(cls, idLogin):
        try:
            cls.__banco.conectar()
            query = 'DELETE FROM login WHERE idLogin = %s;'
            params = (idLogin,)
            cls.__banco.alterarDados(query, params)
            return True
        except Exception as e:
            print(f"Erro ao deletar login: {e}")
            return False
        finally:
            cls.__banco.desconectar()


    # =================== validar ===================
    def validarLogin(self):
        self.__banco.conectar()

        query = "SELECT * FROM login WHERE email = %s;"
        parametro = [self.getEmail()]
        resultado = self.__banco.buscar(query, parametro)
        self.__banco.desconectar()

        try:
            if resultado:
                senhaBanco = resultado[3].encode('utf-8')
                senhaUsuario = self.getSenha()

                if Criptografia.validarSenha(senhaUsuario, senhaBanco):
                    self.setIdLogin(resultado[0])
                    self.setIdPessoa(resultado[1])
                    return True
        except Exception as e:
            print(f"Erro na validação de login: {e}")
        return False

if __name__ == "__main__":
    pass
