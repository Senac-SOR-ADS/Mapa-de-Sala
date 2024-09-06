from model.conexao import ConexaoBD

if __name__ == "__main__":

    try:
        db = ConexaoBD()
        db.conectar()

        db.alterarDados("DELETE FROM `sala` WHERE `idSala` = 7")
        db.desconectar()

    except ConnectionError as err:
        raise f"Erro: {err}"
