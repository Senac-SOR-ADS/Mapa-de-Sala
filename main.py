from model.meuModelo import MeuBd

if __name__ == "__main__":

    try:
        db = MeuBd()
        db.conectar()

        '''Em produção é necessario tirar o print do
        return de dentro das funções'''

        db.buscar_um("SELECT * FROM testetabela WHERE id=1")
        db.buscar_todos("SELECT * FasfROM testetabela")

        db.desconectar()

    except ConnectionError as err:
        raise f"Erro: {err}"
