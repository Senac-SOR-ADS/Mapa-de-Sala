from App.model.conexao import ConexaoBD
from App.model.logger import logger_model

class Sala:
    __banco = ConexaoBD()

    def __init__(self, nome, tipo, predio, equipamentos, capacidade, observacao) -> None:
        self.nome = nome
        self.tipo = tipo
        self.predio = predio
        self.__equipamentos = equipamentos
        self.capacidade = capacidade
        self.observacao = observacao
        self.__id = None
        
    # =================== Getters ===================
    def get_id(self): return self.__id
    def get_equipamentos(self): return self.__equipamentos
    def get_nome(self): return self.nome

    # =================== Setters ===================
    def __set_id(self, id): self.__id = id
    def set_equipamentos(self, equipamentos): self.__equipamentos = equipamentos

    # =================== getListaSala ===================
    @classmethod
    def getListaSala(cls, dados):
        logger_model.debug("[BUSCA] Iniciando conversão de %d registros de sala para objetos Sala", len(dados))
        listaSala = []
        
        try:
            for sala in dados:
                objetoSala = cls(sala[1], sala[2], sala[3], sala[4], sala[5], sala[6])
                objetoSala.__set_id(sala[0])
                listaSala.append(objetoSala)
            
            logger_model.info("[BUSCA] %d objetos Sala criados com sucesso", len(listaSala))
        except Exception as e:
            logger_model.error("[BUSCA] Erro ao criar objetos Sala: %s", e)
        
        return listaSala

    # =================== buscar_sala ===================
    @classmethod
    def buscar_sala(cls):
        logger_model.debug("[BUSCA] Iniciando busca de todas as salas no banco de dados.")
        try:
            cls.__banco.conectar()
            query = '''SELECT * FROM sala;'''
            resultado = cls.__banco.buscarTodos(query)
            logger_model.info("[BUSCA] %d salas encontradas", len(resultado))
        except Exception as e:
            logger_model.error("[BUSCA] Erro ao buscar salas: %s", e)
            resultado = []
        finally:
            cls.__banco.desconectar()

        if resultado:
            logger_model.debug("[BUSCA] Convertendo %d registros de sala para objetos Sala", len(resultado))
            return cls.getListaSala(resultado)
        else:
            logger_model.warning("[BUSCA] Nenhuma sala encontrada.")
            return []

    # =================== buscar_sala_predio1 ===================
    @classmethod
    def buscar_sala_predio1(cls):
        logger_model.debug("[BUSCA] Buscando salas do prédio 1 no banco de dados.")
        try:
            cls.__banco.conectar()
            query = '''SELECT * FROM sala WHERE predio = 1;'''
            resultado = cls.__banco.buscarTodos(query)
            logger_model.info("[BUSCA] %d salas encontradas no prédio 1", len(resultado))
        except Exception as e:
            logger_model.error("[BUSCA] Erro ao buscar salas do prédio 1: %s", e)
            resultado = []
        finally:
            cls.__banco.desconectar()

        if resultado:
            return resultado
        else:
            logger_model.warning("[BUSCA] Nenhuma sala encontrada no prédio 1.")
            return []

    # =================== buscar_sala_predio2 ===================
    @classmethod
    def buscar_sala_predio2(cls):
        logger_model.debug("[BUSCA] Buscando salas do prédio 2 no banco de dados.")
        try:
            cls.__banco.conectar()
            query = '''SELECT * FROM sala WHERE predio = 2;'''
            resultado = cls.__banco.buscarTodos(query)
            logger_model.info("[BUSCA] %d salas encontradas no prédio 2", len(resultado))
        except Exception as e:
            logger_model.error("[BUSCA] Erro ao buscar salas do prédio 2: %s", e)
            resultado = []
        finally:
            cls.__banco.desconectar()

        if resultado:
            return resultado
        else:
            logger_model.warning("[BUSCA] Nenhuma sala encontrada no prédio 2.")
            return []

    # =================== buscar_nomeId_sala ===================
    @classmethod
    def buscar_nomeId_sala(cls):
        logger_model.debug("[BUSCA] Buscando nome e ID de todas as salas.")
        try:
            cls.__banco.conectar()
            query = '''SELECT idSala, nome FROM sala;'''
            resultado = cls.__banco.buscarTodos(query)
            logger_model.info("[BUSCA] %d registros de salas encontrados", len(resultado))
        except Exception as e:
            logger_model.error("[BUSCA] Erro ao buscar nome e ID das salas: %s", e)
            resultado = []
        finally:
            cls.__banco.desconectar()

        if resultado:
            return resultado
        else:
            logger_model.warning("[BUSCA] Nenhum registro de salas encontrado.")
            return []

    # =================== Buscar ID ===================
    @classmethod
    def pesquisar_id(cls, idSala):
        logger_model.info("[BUSCA ID] Pesquisando sala com ID %s", idSala)
        try:
            cls.__banco.conectar()
            query = "SELECT * FROM sala WHERE idSala = %s"
            resultado = cls.__banco.buscar(query, (idSala,))
            
            if resultado:
                logger_model.info("[BUSCA ID] Sala encontrada: %s", resultado)
            else:
                logger_model.warning("[BUSCA ID] Nenhuma sala encontrada com ID %s", idSala)
            return resultado
        except Exception as e:
            logger_model.error("[BUSCA ID] Erro ao pesquisar sala por ID %s: %s", idSala, e)
            return None
        finally:
            cls.__banco.desconectar()

    # =================== cadastrar Sala ===================
    def cadastrar_sala(self):
        logger_model.info("[CADASTRO] Iniciando cadastro da sala: %s", self.nome)
        try:
            self.__banco.conectar()
            query = '''INSERT INTO `sala`(`nome`, `tipo`, `predio`, `equipamentos`, `capacidade`, `observacao`) 
                    VALUES (%s, %s, %s, %s, %s, %s);'''
            parametros = (self.nome, self.tipo, self.predio, self.__equipamentos, self.capacidade, self.observacao)
            resultado = self.__banco.alterarDados(query, parametros)
            
            if resultado:
                logger_model.info("[CADASTRO] Sala '%s' cadastrada com sucesso", self.nome)
            else:
                logger_model.warning("[CADASTRO] Nenhuma linha afetada ao cadastrar a sala '%s'", self.nome)

            return resultado
        except Exception as e:
            logger_model.error("[CADASTRO] Erro ao cadastrar a sala '%s'. Erro: %s", self.nome, e)
            return None
        finally:
            self.__banco.desconectar()

    # =================== deletar Sala ===================
    @classmethod
    def deletar(cls, idSala):
        logger_model.warning("[DELEÇÃO] Deletando sala com ID: %s", idSala)
        
        try:
            cls.__banco.conectar()
            query = "DELETE FROM sala WHERE idSala = %s"
            parametro = [idSala]
            resultado = cls.__banco.alterarDados(query, parametro)
            
            if resultado.rowcount == 0:
                logger_model.warning("[DELEÇÃO] Nenhuma sala encontrada com ID: %s", idSala)
                return False
            
            logger_model.info("[DELEÇÃO] Sala com ID %s deletada com sucesso", idSala)
            return True
            
        except Exception as e:
            logger_model.error("[ERRO] Falha ao deletar sala com ID %s: %s", idSala, str(e))
            return False
            
        finally:
            cls.__banco.desconectar()

    # =================== atualizar Sala ===================
    @classmethod
    def atualizar(cls, nome, tipo, predio, equipamento, capacidade, observacao, idSala):
        logger_model.info("[ATUALIZAÇÃO] Atualizando sala com ID: %s", idSala)
        
        try:
            cls.__banco.conectar()
            query = "UPDATE sala SET `nome`= %s, `tipo`= %s, `predio`= %s, `equipamentos`= %s, `capacidade`= %s, `observacao`= %s WHERE idSala = %s"
            parametro = [nome, tipo, predio, equipamento, capacidade, observacao, idSala]
            resultado = cls.__banco.alterarDados(query, parametro)
            
            if resultado.rowcount == 0:
                logger_model.warning("[ATUALIZAÇÃO] Nenhuma sala encontrada com ID: %s", idSala)
                return False
            
            logger_model.info("[ATUALIZAÇÃO] Sala com ID %s atualizada com sucesso", idSala)
            return True

        except Exception as e:
            logger_model.error("[ERRO] Falha ao atualizar sala com ID %s: %s", idSala, str(e))
            return False

        finally:
            cls.__banco.desconectar()

if __name__ == "__main__":
    pass
