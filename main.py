from model.conexao import ConexaoBD


if __name__ == "__main__":

    try:
        db = ConexaoBD()

        db.conectar()

        db.buscar_um("SELECT * FROM sala WHERE idSala=1")
        db.buscar_todos("SELECT * FROM sala")

        db.desconectar()

    except ConnectionError as err:
        raise f"Erro: {err}"
