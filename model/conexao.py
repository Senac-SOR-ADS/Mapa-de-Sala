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

            # print("Conectado")  # Debug
            return self.__conexao().is_connected()

        except connector.Error as err:
            self.__conn = None
            print(f"Erro: {err}")
            return False

    def desconectar(self) -> bool:
        if self.__conexao().is_connected():
            # print("Desconectado") # Debug
            self.__conexao().close()

    def buscar(self, query, param=None) -> list:
        try:
            cur = self.__conexao().cursor()
            cur.execute(query, param)
            resultado = cur.fetchone()

            print(f"Busca única: {resultado}")
        except Exception as e:
            print(f"Erro ao buscar um: {e}")
            resultado = list()
        finally:
            if cur:
                cur.close()
            return resultado

    def buscarTodos(self, query, param=None) -> list:
        try:
            cur = self.__conexao().cursor()
            cur.execute(query, param)
            resultado = cur.fetchall()

            print(f"Busca completa: {resultado}")
        except Exception as e:
            print(f"Erro ao buscar todos: {e}")
            resultado = list()

        finally:
            if cur:
                cur.close()
            return resultado

    def alterarDados(self, query, param=None):
        try:
            cur = self.__conexao().cursor()
            cur.execute(query, param)
            self.commit()
            print("Dados alterados com sucesso")
            return cur

        except Exception as e:
            print(f"Erro ao alterar dados: {e}")

    def commit(self):
        self.__conexao().commit()

    def __conexao(self):
        return self.__conn
