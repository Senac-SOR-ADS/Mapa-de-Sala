import os
import mysql.connector as connector
from dotenv import load_dotenv

load_dotenv()


class MeuBd:

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

            if not self.__conn.is_connected():
                raise Exception('Não foi conectado')

            print("Conectado")  # Debug
            return self.__conn.is_connected()
        except connector.Error as err:
            self.__conn = None
            print(f"Erro: {err}")
            return False

    def desconectar(self):
        if self.__conn.is_connected():
            print("Desconectado")
            self.__conn.close()

    def commit(self):
        self.__conn.commit()

    def buscar_um(self, query, param=None) -> list:
        try:
            cur = self.__conn.cursor()
            cur.execute(query, param)
            resultado = cur.fetchall()

            print(f"Busca única: {resultado}")

        except Exception:
            resultado = list()

        finally:
            cur.close()
            return resultado

    def buscar_todos(self, query, param=None) -> list:
        try:
            cur = self.__conn.cursor()
            cur.execute(query, param)
            resultado = cur.fetchall()

            print(f"Busca completa: {resultado}")

        except Exception:
            resultado = list()

        finally:
            cur.close()
            return resultado
