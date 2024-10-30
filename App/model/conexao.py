import os
import mysql.connector as connector
from dotenv import load_dotenv

load_dotenv()


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

            return self.__conexao().is_connected()

        except connector.Error as err:
            self.__conn = connector.CMySQLConnection()
            return False

    def desconectar(self) -> bool:
        if self.__conexao().is_connected():
            self.__conexao().close()

    def buscar(self, query, param=None) -> list:
        try:
            cur = self.__conexao().cursor()
            cur.execute(query, param)
            resultado = cur.fetchone()

        except Exception as e:
            resultado = list()
        finally:
            return resultado

    def buscarTodos(self, query, param=None) -> list:
        try:
            cur = self.__conexao().cursor()
            cur.execute(query, param)
            resultado = cur.fetchall()

        except Exception as e:
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
            print('erro: ', e)
            cur = None

    def commit(self):
        self.__conexao().commit()

    def __conexao(self):
        return self.__conn

if __name__ == "__main__":
    bd = ConexaoBD()
    bd.conectar()
    bd.desconectar()