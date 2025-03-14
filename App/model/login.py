from App.model.conexao import ConexaoBD
from App.model.criptografia import Criptografia
from App.model.logger import logger_model

class Login:
    def __init__(self, email=None, senha=None, nivel_acesso='user') -> None:
        self.__banco = ConexaoBD()
        self.__email, self.__senha, self.__idLogin, self.__idPessoa, self.__nivelAcesso = email, senha, None, None, nivel_acesso

    # =================== Getters ===================
    def getIdLogin(self): return self.__idLogin
    def getIdPessoa(self): return self.__idPessoa
    def getEmail(self): return self.__email
    def getSenha(self): return self.__senha
    def getNivelAcesso(self): return self.__nivelAcesso

    # =================== Setters ===================
    def setIdLogin(self, id): self.__idLogin = id
    def setIdPessoa(self, id): self.__idPessoa = id
    def setEmail(self, email): self.__email = email
    def setSenha(self, senha): self.__senha = senha
    def setNivelAcesso(self, nivel_acesso): self.__nivelAcesso = nivel_acesso

    # =================== cadastrar Login ===================
    def cadastrar(self, idPessoa, cpf_cnpj, email, cargo):
        self.setIdPessoa(idPessoa)
        self.setEmail(email)
        self.setSenha(cpf_cnpj)
        
        senha_criptografada = Criptografia.criptografarSenha(cpf_cnpj)
        nivelAcesso = {"Administrador": "admin", "Suporte": "suporte"}.get(cargo, "user")

        try:
            self.__banco.conectar()
            query_login = """
                INSERT INTO login (idPessoa, email, senha, nivelAcesso)
                VALUES (%s, %s, %s, %s)
            """
            self.__banco.alterarDados(query_login, (idPessoa, email, senha_criptografada, nivelAcesso))
            
            logger_model.success("[CADASTRO] Login cadastrado com sucesso - ID: %s, Email: %s, Nível de Acesso: %s", idPessoa, email, nivelAcesso)
            return True
        
        except Exception as e:
            logger_model.error("[CADASTRO] Erro ao cadastrar login - Email: %s, Erro: %s", email, str(e))
            return False
        
        finally:
            self.__banco.desconectar()
            logger_model.debug("[CADASTRO] Conexão com o banco encerrada.")

    # =================== Atualizar Módulo WEB ===================
    def atualizarWEB(self, idLogin, email, cargo, senha=None):
        """Atualiza o email, nível de acesso e, opcionalmente, a senha de um usuário, com base no cargo."""
        
        nivelAcesso = {"Administrador": "admin", "Suporte": "suporte"}.get(cargo, "user")

        try:
            self.__banco.conectar()

            if senha:
                query_update = 'UPDATE login SET email = %s, nivelAcesso = %s, senha = %s WHERE idLogin = %s'
                valores = (email, nivelAcesso, Criptografia.criptografarSenha(senha), idLogin)
            else:
                query_update = 'UPDATE login SET email = %s, nivelAcesso = %s WHERE idLogin = %s'
                valores = (email, nivelAcesso, idLogin)

            self.__banco.alterarDados(query_update, valores)
            logger_model.info("[ATUALIZACAO] Cadastro atualizado com sucesso - ID: %s, Email: %s, Nível de Acesso: %s", idLogin, email, nivelAcesso)
            return True
        except Exception as e:
            logger_model.error("[ATUALIZACAO] Erro ao atualizar cadastro - ID: %s, Erro: %s", idLogin, str(e))
            return False
        finally:
            self.__banco.desconectar()
            logger_model.debug("[ATUALIZACAO] Conexão com o banco de dados encerrada.")


    # =================== Atualizar Módulo Desktop ===================
    def atualizar(self, idLogin, email, acesso, senha):
        """Atualiza o email, nível de acesso e a senha de um usuário."""
        
        senha = Criptografia.criptografarSenha(senha)

        try:
            self.__banco.conectar()
            query_update = '''
                UPDATE login
                SET email = %s, nivelAcesso = %s, senha = %s
                WHERE idLogin = %s
            '''
            valores = (email, acesso, senha, idLogin)
            self.__banco.alterarDados(query_update, valores)
            logger_model.info("[ATUALIZACAO] Cadastro atualizado com sucesso - ID: %s, Email: %s, Nível de Acesso: %s", idLogin, email, acesso)
            return True
        except Exception as e:
            logger_model.error("[ATUALIZACAO] Erro ao atualizar cadastro - ID: %s, Erro: %s", idLogin, str(e))
            return False
        finally:
            self.__banco.desconectar()
            logger_model.debug("[ATUALIZACAO] Conexão com o banco de dados encerrada.")

    # =================== buscar Login ===================
    def buscar(self, idLogin):
        try:
            self.__banco.conectar()
            query = "SELECT * FROM login WHERE idLogin = %s;"
            resultado = self.__banco.buscar(query, (idLogin,))
            
            if resultado:
                self.setIdLogin(resultado[0])
                self.setIdPessoa(resultado[1])
                self.setEmail(resultado[2])
                self.setSenha(resultado[3])
                self.setNivelAcesso(resultado[4])
                
                logger_model.info("[BUSCA ID] Login encontrado - ID: %s, Email: %s", idLogin, resultado[2])
                return True
            
            logger_model.warning("[BUSCA ID] Nenhum login encontrado - ID: %s", idLogin)
            return False

        except Exception as e:
            logger_model.error("[BUSCA ID] Erro ao buscar login - ID: %s, Erro: %s", idLogin, str(e))
            return False

        finally:
            self.__banco.desconectar()
            logger_model.debug("[BUSCA ID] Conexão com o banco de dados encerrada.")

    # =================== buscar todos ===================
    @classmethod
    def buscar_todos(cls):
        banco = ConexaoBD()
        try:
            banco.conectar()
            resultado = banco.buscarTodos("SELECT * FROM login")
            logger_model.info("[BUSCA] Todos os logins foram buscados - Total: %d", len(resultado))
            return resultado
        except Exception as e:
            logger_model.error("[BUSCA] Erro ao buscar todos os logins - Erro: %s", str(e))
            return []
        finally:
            banco.desconectar()
            logger_model.debug("[BUSCA] Conexão com o banco de dados encerrada.")

    # =================== Buscar ID ===================
    @classmethod
    def pesquisar_id(cls, idLogin):
        banco = ConexaoBD()
        try:
            banco.conectar()
            resposta = banco.buscar('SELECT * FROM login WHERE idLogin = %s;', (idLogin,))
            
            if resposta:
                logger_model.info("[BUSCA ID] Login encontrado - ID: %s", idLogin)
            else:
                logger_model.warning("[BUSCA ID] Nenhum login encontrado - ID: %s", idLogin)
            
            return resposta if resposta else False

        except Exception as e:
            logger_model.error("[BUSCA ID] Erro ao pesquisar login - ID: %s, Erro: %s", idLogin, str(e))
            return False

        finally:
            banco.desconectar()
            logger_model.debug("[BUSCA ID] Conexão com o banco de dados encerrada.")

    # =================== deletar Login ===================
    @classmethod
    def deletar(cls, idLogin):
        banco = ConexaoBD()
        try:
            banco.conectar()
            banco.alterarDados('DELETE FROM login WHERE idLogin = %s;', (idLogin,))
            logger_model.info("[DELECAO] Login deletado com sucesso - ID: %s", idLogin)
            return True
        except Exception as e:
            logger_model.error("[DELECAO] Erro ao deletar login - ID: %s, Erro: %s", idLogin, str(e))
            return False
        finally:
            banco.desconectar()
            logger_model.debug("[DELECAO] Conexão com o banco de dados encerrada.")

    # =================== validar login ===================
    def validarLogin(self):
        email = self.getEmail()
        senha = self.getSenha()
        query = "SELECT * FROM login WHERE email = %s;"

        try:
            self.__banco.conectar()
            resultado = self.__banco.buscar(query, [email])

            if not resultado or not resultado[3]:
                logger_model.warning("[VALIDACAO] Usuário encontrado, mas senha não cadastrada - Email: %s", email)
                return False

            senha_hash = resultado[3].encode('utf-8')
            if Criptografia.validarSenha(senha, senha_hash):
                self.setIdLogin(resultado[0])
                self.setIdPessoa(resultado[1])
                self.setNivelAcesso(resultado[4])
                logger_model.info("[VALIDACAO] Login validado com sucesso - Email: %s", email)
                return True

        except Exception as e:
            logger_model.error("[VALIDACAO] Erro na validação de login - Email: %s, Erro: %s", email, str(e))

        finally:
            self.__banco.desconectar()
            logger_model.debug("[VALIDACAO] Conexão com o banco de dados encerrada.")

        return False

if __name__ == "__main__":
    pass
