import os
import mysql.connector as connector
from dotenv import load_dotenv
from App.model.logger import logger_conexao

# =================== Configuração ===================
load_dotenv(override=True)

# =================== Classe ConexaoBD ===================
class ConexaoBD:
    def __init__(self):
        self.__host = os.getenv("HOST")
        self.__username = os.getenv("LOGIN")
        self.__password = os.getenv("PASSWORD", "")
        self.__database = os.getenv("DATABASE")
        self.__conn = None
        self.__in_transaction = False

        if not all([self.__host, self.__username, self.__database]):
            mensagem = "[ERRO] Variáveis de ambiente do banco de dados não estão corretamente configuradas."
            logger_conexao.error(mensagem)
            raise ValueError(mensagem)

    def __enter__(self):
        self.conectar()
        self.__in_transaction = False
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            if self.__in_transaction:
                self.rollback()
            logger_conexao.error(f"[ERRO] Exceção: {exc_type} | {exc_value} | Traceback: {traceback.format_exception(exc_type, exc_value, traceback)}")
        elif self.__in_transaction:
            self.commit()
        self.desconectar()

    # =================== Propriedades ===================
    @property
    def conexao_valida(self):
        return self.__conn and self.__conn.is_connected()

    @property
    def status_conexao(self):
        return "Conectado" if self.conexao_valida else "Desconectado"

    @property
    def nome_banco(self):
        return self.__database

    # =================== Conectar ===================
    def conectar(self) -> bool:
        if self.conexao_valida:
            return True
        try:
            self.desconectar()
            self.__conn = connector.connect(
                user=self.__username, password=self.__password,
                host=self.__host, database=self.__database,
            )
            if not self.__conn.is_connected():
                raise Exception("Não foi possível conectar ao banco de dados")
            logger_conexao.info("[CONEXAO] Conexão realizada com sucesso! Banco: %s, Host: %s", self.__database, self.__host)
            return True
        except connector.OperationalError as err:
            self.__conn = None
            logger_conexao.error("[ERRO] Falha ao conectar no banco '%s' (%s) | Detalhes: %s", self.__database, self.__host, err)
        except connector.Error as err:
            self.__conn = None
            logger_conexao.error("[ERRO] Erro de conexão no banco '%s' | Detalhes: %s", self.__database, err)
        except Exception as e:
            self.__conn = None
            logger_conexao.critical("[ERRO] Erro inesperado ao tentar conectar: %s", e)
        return False

    # =================== Desconectar ===================
    def desconectar(self) -> bool:
        if self.conexao_valida:
            try:
                self.__conn.close()
                self.__conn = None
                logger_conexao.info("[CONEXAO] Conexão com o banco '%s' encerrada com sucesso.", self.__database)
                return True
            except Exception as e:
                logger_conexao.error("[ERRO] Falha ao desconectar do banco '%s' | Detalhes: %s", self.__database, e)
        return False

    # =================== Buscar ===================
    def buscar(self, query, param=None):
        try:
            if not self.conexao_valida:
                logger_conexao.warning("[ERRO] Conexão inválida ao tentar buscar dados. Tentando reconectar...")
                if not self.conectar():
                    raise Exception("Não foi possível estabelecer a conexão com o banco de dados.")
            with self.__conn.cursor() as cur:
                cur.execute(query, param if param else ())
                resultado = cur.fetchone()
                logger_conexao.info("[BUSCA] Consulta realizada com sucesso: %s", query)
                return resultado
        except connector.ProgrammingError as e:
            logger_conexao.error("[ERRO] Erro de sintaxe no SQL. Detalhes: %s", e)
        except connector.OperationalError as e:
            logger_conexao.error("[ERRO] Problema operacional na conexão. Detalhes: %s", e)
        except Exception as e:
            logger_conexao.error("[ERRO] Falha na busca de dados | Query: %s | Detalhes: %s", query, e)
        return None

    # =================== Buscar Todos ===================
    def buscarTodos(self, query, param=None):
        try:
            if not self.conexao_valida:
                logger_conexao.warning("[ERRO] Conexão inválida ao tentar buscar dados. Tentando reconectar...")
                if not self.conectar():
                    raise Exception("Não foi possível estabelecer a conexão com o banco de dados.")
            with self.__conn.cursor() as cur:
                cur.execute(query, param if param else ())
                resultado = cur.fetchall() or []
                logger_conexao.info("[BUSCA TODOS] Consulta múltipla realizada com sucesso: %s", query)
                return resultado
        except connector.ProgrammingError as e:
            logger_conexao.error("[ERRO] Erro de sintaxe no SQL. Detalhes: %s", e)
        except connector.OperationalError as e:
            logger_conexao.error("[ERRO] Problema operacional na conexão. Detalhes: %s", e)
        except Exception as e:
            logger_conexao.error("[ERRO] Falha na busca de múltiplos dados | Query: %s | Detalhes: %s", query, e)
        return []

    # =================== Alterar Dados ===================
    def alterarDados(self, query, param=None):
        try:
            if not self.conexao_valida:
                logger_conexao.warning("[ERRO] Conexão inválida ao tentar alterar dados. Tentando reconectar...")
                if not self.conectar():
                    raise Exception("Não foi possível estabelecer a conexão com o banco de dados.")
            
            with self.__conn.cursor() as cur:
                cur.execute(query, param if param else ())
                self.commit()
                logger_conexao.info("[ATUALIZACAO] Dados alterados com sucesso: %s", query)
                return cur
        except (connector.ProgrammingError, connector.OperationalError) as e:
            self.__conn.rollback()
            logger_conexao.error("[ERRO] Falha ao alterar dados | Query: %s | Detalhes: %s", query, e)
            raise
        except Exception as e:
            self.__conn.rollback()
            logger_conexao.error("[ERRO] Falha inesperada ao alterar dados | Query: %s | Detalhes: %s", query, e)
            raise

    # =================== Commit ===================
    def commit(self):
        try:
            if self.__conn:
                self.__conn.commit()
                self.__in_transaction = False
                logger_conexao.info("[COMMIT] Commit realizado com sucesso.")
        except connector.Error as e:
            if self.__conn:
                self.__conn.rollback()
            logger_conexao.error("[ERRO] Falha ao executar commit. Alterações revertidas. Detalhes: %s", e)
        except Exception as e:
            if self.__conn:
                self.__conn.rollback()
            logger_conexao.error("[ERRO] Erro inesperado ao executar commit. Alterações revertidas. Detalhes: %s", e)

    # =================== Rollback ===================
    def rollback(self):
        try:
            if self.__conn:
                self.__conn.rollback()
                logger_conexao.info("[ROLLBACK] Transação revertida com sucesso.")
        except Exception as e:
            logger_conexao.error("[ERRO] Falha ao reverter transação. Detalhes: %s", e)

if __name__ == "__main__":
    with ConexaoBD() as bd:
        pass
