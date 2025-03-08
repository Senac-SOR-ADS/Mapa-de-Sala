from App.model.conexao import ConexaoBD
from App.model.logger import logger_model

class Pessoa:
    __banco = ConexaoBD()

    def __init__(self) -> None:
        self.__idPessoa = self.__nome = self.__cpf_cnpj = None
        self.__nascimento = self.__telefone = self.__email = self.__cargo = None

    # =================== Getters ===================
    def get_idPessoa(self): return self.__idPessoa
    def get_nome(self): return self.__nome
    def get_cpf_cnpj(self): return self.__cpf_cnpj
    def get_nascimento(self): return self.__nascimento
    def get_telefone(self): return self.__telefone
    def get_email(self): return self.__email
    def get_cargo(self): return self.__cargo

    # =================== Setters ===================
    def __set_idPessoa(self, id): self.__idPessoa = id
    def __set_nome(self, nome): self.__nome = nome
    def __set_cpf_cnpj(self, cpf_cnpj): self.__cpf_cnpj = cpf_cnpj
    def __set_nascimento(self, nascimento): self.__nascimento = nascimento
    def __set_telefone(self, telefone): self.__telefone = telefone
    def __set_email(self, email): self.__email = email
    def __set_cargo(self, cargo): self.__cargo = cargo

    # =================== cadastrar Pessoa ===================
    def cadastrar(self, nome, cpf_cnpj, nascimento, telefone, email, cargo):
        logger_model.info("[CADASTRO] Iniciando processo de cadastro de nova pessoa: Nome: '%s'.", nome)
        
        self.__set_nome(nome)
        self.__set_cpf_cnpj(cpf_cnpj)
        self.__set_nascimento(nascimento)
        self.__set_telefone(telefone)
        self.__set_email(email)
        self.__set_cargo(cargo)

        try:
            self.__banco.conectar()
            logger_model.debug("[CADASTRO] Conexão com o banco estabelecida.")
            
            query_pessoa = '''
            INSERT INTO pessoa (nome, CPF_CNPJ, nascimento, telefone, email, cargo)
            VALUES (%s, %s, %s, %s, %s, %s)
            '''
            params_pessoa = (self.get_nome(), self.get_cpf_cnpj(), self.get_nascimento(),
                            self.get_telefone(), self.get_email(), self.get_cargo())
            resposta = self.__banco.alterarDados(query_pessoa, params_pessoa)
            
            self.__set_idPessoa(resposta.lastrowid)
            logger_model.success("[CADASTRO] Cadastro realizado com sucesso. Nome: '%s', ID: %s", self.get_nome(), self.get_idPessoa())
            return self.get_idPessoa()
        except Exception as e:
            logger_model.error("[CADASTRO] Falha no cadastro de pessoa: Nome: '%s', Erro: %s", nome, str(e))
            return None
        finally:
            self.__banco.desconectar()
            logger_model.debug("[CADASTRO] Conexão com o banco encerrada.")

    # =================== buscar Pessoa ===================
    @classmethod
    def buscar(cls):
        logger_model.info("[BUSCA] Iniciando busca por todas as pessoas cadastradas.")
        try:
            cls.__banco.conectar()
            logger_model.debug("[BUSCA] Conexão com o banco estabelecida.")
            
            query = 'SELECT idPessoa, nome FROM pessoa;'
            resposta = cls.__banco.buscarTodos(query)
            
            logger_model.success("[BUSCA] Busca realizada com sucesso.")
            return resposta
        except Exception as e:
            logger_model.error("[BUSCA] Erro ao buscar lista de pessoas: %s", str(e))
            return False
        finally:
            cls.__banco.desconectar()
            logger_model.debug("[BUSCA] Conexão com o banco encerrada.")

    # =================== buscar Id ===================
    @classmethod
    def pesquisar_id(cls, idPessoa):
        logger_model.info("[BUSCA ID] Pesquisando informações da pessoa com ID %s.", idPessoa)
        try:
            cls.__banco.conectar()
            logger_model.debug("[BUSCA ID] Conexão com o banco estabelecida.")
            
            query = 'SELECT * FROM pessoa WHERE idPessoa = %s;'
            resposta = cls.__banco.buscar(query, (idPessoa,))
            
            logger_model.success("[BUSCA ID] Pessoa encontrada com sucesso. ID: %s", idPessoa)
            return resposta
        except Exception as e:
            logger_model.error("[BUSCA ID] Erro ao pesquisar pessoa com ID %s: %s", idPessoa, str(e))
            return False
        finally:
            cls.__banco.desconectar()
            logger_model.debug("[BUSCA ID] Conexão com o banco encerrada.")

    # =================== atualizar Pessoa ===================
    def atualizar(self, idPessoa, nome, cpf_cnpj, nascimento, telefone, email, cargo):
        logger_model.info("[ATUALIZACAO] Iniciando atualização dos dados da pessoa com ID %s: Novo nome: '%s'.", idPessoa, nome)
        self.__set_idPessoa(idPessoa)
        self.__set_nome(nome)
        self.__set_cpf_cnpj(cpf_cnpj)
        self.__set_nascimento(nascimento)
        self.__set_telefone(telefone)
        self.__set_email(email)
        self.__set_cargo(cargo)

        try:
            self.__banco.conectar()
            logger_model.debug("[ATUALIZACAO] Conexão com o banco estabelecida.")
            
            query = '''
                UPDATE pessoa 
                SET nome = %s, CPF_CNPJ = %s, nascimento = %s, telefone = %s, email = %s, cargo = %s 
                WHERE idPessoa = %s
            '''
            params = (self.get_nome(), self.get_cpf_cnpj(), self.get_nascimento(),
                    self.get_telefone(), self.get_email(), self.get_cargo(), self.get_idPessoa())
            
            self.__banco.alterarDados(query, params)
            logger_model.success("[ATUALIZACAO] Atualização concluída com sucesso para a pessoa ID %s: Novo nome: '%s'.", idPessoa, nome)
            return True
        except Exception as e:
            logger_model.error("[ATUALIZACAO] Falha ao atualizar pessoa com ID %s: Erro: %s", idPessoa, str(e))
            return False
        finally:
            self.__banco.desconectar()
            logger_model.debug("[ATUALIZACAO] Conexão com o banco encerrada.")

    # =================== deletar Pessoa ===================
    @classmethod
    def deletar(cls, idPessoa):
        logger_model.warning("[DELECAO] Iniciando exclusão da pessoa com ID %s.", idPessoa)
        try:
            cls.__banco.conectar()
            logger_model.debug("[DELECAO] Conexão com o banco estabelecida.")
            query = 'DELETE FROM pessoa WHERE idPessoa = %s;'
            cls.__banco.alterarDados(query, (idPessoa,))
            logger_model.success("[DELECAO] Pessoa ID %s deletada com sucesso.", idPessoa)
            return True
        except Exception as e:
            logger_model.error("[DELECAO] Erro ao deletar pessoa ID %s: Erro: %s", idPessoa, str(e))
            return False
        finally:
            cls.__banco.desconectar()
            logger_model.debug("[DELECAO] Conexão com o banco encerrada.")

if __name__ == "__main__":
    pass
