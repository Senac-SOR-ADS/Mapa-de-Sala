from App.model.logger import logger_model
from App.model.conexao import ConexaoBD

class Area:
    __banco = ConexaoBD()

    def __init__(self, nome) -> None:
        self.__nome = nome

    # =================== Getters ===================
    def get_nome(self): return self.__nome

    # =================== Setters ===================
    def set_nome(self, nome): self.__nome = nome

    # =================== cadastrar_area ===================
    def cadastrar_area(self):
        """Uma função para fazer o cadastro de uma área"""
        logger_model.debug("[CADASTRO] %s", self.__nome)
        try:
            self.__banco.conectar()
            query = "INSERT INTO area (nome) VALUES (%s)"
            parametro = [self.__nome]
            if self.__banco.alterarDados(query, parametro):
                logger_model.success("[CADASTRO] %s cadastrada com sucesso!", self.__nome)
                return True
            else:
                logger_model.error("[CADASTRO] Falha ao cadastrar a área '%s'.", self.__nome)
                return False
        except Exception as e:
            logger_model.error("[CADASTRO] Erro ao cadastrar a área '%s': %s", self.__nome, str(e))
            return False
        finally:
            self.__banco.desconectar()
            logger_model.debug("[CADASTRO] Conexão com o banco encerrada.")

    # =================== buscar_nome_area ===================
    @classmethod
    def buscar_nome_area(cls, idArea):
        """Uma função que devolve o nome da área"""
        logger_model.debug("[BUSCA ID] Buscando nome da área com ID: %s", idArea)
        try:
            cls.__banco.conectar()
            query = "SELECT nome FROM area WHERE idArea = %s"
            param = [idArea]
            resultado = cls.__banco.buscar(query, param)
            if resultado:
                logger_model.info("[BUSCA ID] Área '%s' encontrada com ID: %s", resultado[0], idArea)
                return resultado[0]
            logger_model.warning("[BUSCA ID] Nenhuma área encontrada para o ID: %s", idArea)
            return None
        except Exception as e:
            logger_model.error("[BUSCA ID] Erro ao buscar área com ID %s: %s", idArea, str(e))
            return None
        finally:
            cls.__banco.desconectar()
            logger_model.debug("[BUSCA ID] Conexão com o banco encerrada.")

    # =================== consulta_areas ===================
    @classmethod
    def consulta_areas(cls):
        """Uma função que devolve todas as áreas"""
        logger_model.debug("[BUSCA] Iniciando consulta de todas as áreas")
        try:
            cls.__banco.conectar()
            query = "SELECT * FROM area"
            resultado = cls.__banco.buscarTodos(query)
            logger_model.info("[BUSCA] Total de áreas encontradas: %d", len(resultado))
            return resultado
        except Exception as e:
            logger_model.error("[BUSCA] Erro ao consultar áreas: %s", str(e))
            return []
        finally:
            cls.__banco.desconectar()
            logger_model.debug("[BUSCA] Conexão com o banco encerrada.")

    # =================== consulta_area_curso ===================
    def consulta_area_curso(self):
        """Uma função que devolve a área junto com os nomes de cursos dessa área"""
        logger_model.debug("[BUSCA] Iniciando consulta de áreas e cursos associados")
        try:
            self.__banco.conectar()
            query = "SELECT a.nome, c.nome FROM area a JOIN curso c ON a.idArea = c.idArea"
            resultado = self.__banco.buscarTodos(query)
            logger_model.info("[BUSCA] Consulta concluída. Registros encontrados: %d", len(resultado))
            return resultado
        except Exception as e:
            logger_model.error("[BUSCA] Erro ao consultar áreas e cursos: %s", str(e))
            return []
        finally:
            self.__banco.desconectar()
            logger_model.debug("[BUSCA] Conexão com o banco encerrada.")

    # =================== consulta_especifica ===================
    def consulta_especifica(self):
        """Uma função que devolve apenas uma área que foi passada"""
        logger_model.debug("[BUSCA] Consultando área específica: %s", self.__nome)
        try:
            self.__banco.conectar()
            query = "SELECT * FROM area WHERE nome = %s"
            parametro = [self.__nome]
            resultado = self.__banco.buscar(query, parametro)
            if resultado:
                logger_model.info("[BUSCA] Área '%s' encontrada", self.__nome)
            else:
                logger_model.warning("[BUSCA] Área '%s' não encontrada", self.__nome)
            return resultado
        except Exception as e:
            logger_model.error("[BUSCA] Erro ao consultar área específica '%s': %s", self.__nome, str(e))
            return None
        finally:
            self.__banco.desconectar()
            logger_model.debug("[BUSCA] Conexão com o banco encerrada.")

    # =================== deletar ===================
    @classmethod
    def deletar(cls, idArea):
        """Exclui uma área com base no ID"""
        logger_model.debug("[DELECAO] Tentando excluir a área com ID: %s", idArea)
        try:
            cls.__banco.conectar()
            query = "DELETE FROM area WHERE idArea = %s"
            parametro = [idArea]
            resultado = cls.__banco.alterarDados(query, parametro)
            if resultado.rowcount:
                logger_model.success("[DELECAO] Área com ID '%s' excluída com sucesso!", idArea)
                return True
            logger_model.warning("[DELECAO] Nenhuma área encontrada para exclusão com ID '%s'.", idArea)
            return False
        except Exception as e:
            logger_model.error("[DELECAO] Erro ao excluir a área com ID '%s': %s", idArea, str(e))
            return False
        finally:
            cls.__banco.desconectar()
            logger_model.debug("[DELECAO] Conexão com o banco encerrada.")

    # =================== atualizar ===================
    @classmethod
    def atualizar(cls, idArea, nome):
        """Atualiza o nome de uma área com base no ID"""
        logger_model.debug("[ATUALIZACAO] Iniciando atualização da área com ID '%s'", idArea)
        try:
            cls.__banco.conectar()
            query = "UPDATE area SET nome = %s WHERE idArea = %s"
            parametro = [nome, idArea]
            resultado = cls.__banco.alterarDados(query, parametro)
            if resultado.rowcount:
                logger_model.success("[ATUALIZACAO] Área com ID '%s' atualizada para '%s'.", idArea, nome)
                return True
            logger_model.warning("[ATUALIZACAO] Falha ao atualizar a área com ID '%s'. Nenhuma alteração realizada.", idArea)
            return False
        except Exception as e:
            logger_model.error("[ATUALIZACAO] Erro ao atualizar a área com ID '%s': %s", idArea, str(e))
            return False
        finally:
            cls.__banco.desconectar()
            logger_model.debug("[ATUALIZACAO] Conexão com o banco encerrada.")

if __name__ == '__main__':
    pass
