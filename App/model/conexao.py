import os
import mysql.connector as connector
from dotenv import load_dotenv
from App.controller.logger import Log

def limparEnv():
    try:
        del os.environ["HOST"]
        del os.environ["LOGIN"]
        del os.environ["PASSWORD"]
        del os.environ["DATABASE"]
    except:
        pass

limparEnv()
load_dotenv()

log = Log('conexao')


class ConexaoBD:

    def __init__(self):
        self.__host = os.getenv("HOST")
        self.__username = os.getenv("LOGIN")
        self.__password = os.getenv("PASSWORD")
        self.__database = os.getenv("DATABASE")
        self.__conn = None

    def conectar(self) -> bool:
        config = {
            'user':     self.__username,
            'password': self.__password,
            'host':     self.__host,
            'database': self.__database
        }

        try:
            self.__conn = connector.connect(**config)

            if not self.__conexao().is_connected():
                raise Exception('Não foi conectado')
            
            log.info("Conexão realizada com sucesso!")
            return self.__conexao().is_connected()

        except connector.Error as err:
            self.__conn = connector.CMySQLConnection()
            log.critical(f"Erro ao conectar | Erro: {err}")
            return False

    def desconectar(self) -> bool:
        if self.__conn and self.__conn.is_connected():
            self.__conn.close()
            log.info("Conexão fechada.")

    def buscar(self, query, param=None) -> list:
        resultado = []
        try:
            cur = self.__conexao().cursor()
            cur.execute(query, param)
            resultado = cur.fetchone()
            cur.close()

        except Exception as e:
            log.error(f"Erro de busca | Erro: {e}")
            log.debug(resultado)
            resultado = list()
        finally:
            return resultado
            

    def buscarTodos(self, query, param=None) -> list:
        try:
            if not self.__conn or not self.__conn.is_connected():
                self.conectar()
            cur = self.__conexao().cursor()
            cur.execute(query, param)
            resultado = cur.fetchall()
            cur.close()

        except Exception as e:
            log.error(f"Erro ao buscar todos os dados | Erro: {e}")
            log.debug(resultado)
            resultado = list()

        finally:
            return resultado

    def alterarDados(self, query, param=None):
        try:
            cur = self.__conexao().cursor()
            cur.execute(query, param)
            self.commit()
            return cur

        except Exception as e:
            log.error(f"Erro ao alterar dados | Erro: {e}")
            log.debug(cur)
            cur = None

    def commit(self):
        self.__conexao().commit()

    def __conexao(self):
        return self.__conn

if __name__ == "__main__":
    bd = ConexaoBD()
    bd.conectar()
    bd.desconectar()