from App.model.conexao import ConexaoBD
from App.model.logger import logger_model

class Equipamentos:
    __banco = ConexaoBD()

    def __init__(self, nome, marca, quantidade, area) -> None:
        self.__nome = nome
        self.__marca = marca
        self.__quantidade = quantidade
        self.__area = area

    # =================== Getters ===================
    def get_nome(self): return self.__nome
    def get_marca(self): return self.__marca
    def get_quantidade(self): return self.__quantidade
    def get_area(self): return self.__area

    # =================== Setters ===================
    def set_nome(self, nome): self.__nome = nome
    def set_marca(self, marca): self.__marca = marca
    def set_quantidade(self, quantidade): self.__quantidade = quantidade
    def set_area(self, area): self.__area = area

    # =================== Cadastrar Equipamento ===================
    def cadastrar_equipamento(self, id_area):
        try:
            logger_model.info("[CADASTRO] Iniciando cadastro de equipamento: %s", self.__nome)
            self.__banco.conectar()
            query = "INSERT INTO `equipamento`(`idArea`, `nome`, `marca`, `quantidade`) VALUES (%s, %s, %s, %s)"
            params = [id_area, self.__nome, self.__marca, self.__quantidade]
            resultado = self.__banco.alterarDados(query, params)
            
            if resultado:
                logger_model.success("[CADASTRO] Equipamento '%s' cadastrado com sucesso.", self.__nome)
            else:
                logger_model.warning("[CADASTRO] Nenhum equipamento foi cadastrado. Verifique os dados.")
            return resultado
        except Exception as e:
            logger_model.error("[CADASTRO] Erro ao cadastrar equipamento '%s'. Erro: %s", self.__nome, e)
            return None
        finally:
            self.__banco.desconectar()
            logger_model.debug("[CADASTRO] Conexão com o banco encerrada.")


    # =================== Retorna Equipamento Reservado ===================
    @classmethod
    def retorna_equipamento_reservado(cls):
        try:
            logger_model.info("[BUSCA] Iniciando busca de equipamentos reservados.")
            cls.__banco.conectar()
            query = "SELECT e.nome FROM equipamento e RIGHT JOIN ocupado o ON o.idEquipamento = e.idEquipamento"
            resultado = cls.__banco.buscarTodos(query)
            
            logger_model.info("[BUSCA] Equipamentos reservados encontrados: %d", len(resultado))
            return resultado
        except Exception as e:
            logger_model.error("[BUSCA] Erro ao buscar equipamentos reservados. Erro: %s", e)
            return []
        finally:
            cls.__banco.desconectar()
            logger_model.debug("[BUSCA] Conexão com o banco encerrada.")

    # =================== Retorna Equipamentos Sem Reserva ===================
    @classmethod
    def retorna_equipamentos_sem_reserva(cls):
        try:
            logger_model.info("[BUSCA] Iniciando busca de equipamentos sem reserva.")
            cls.__banco.conectar()
            query = "SELECT e.nome FROM ocupado o RIGHT JOIN equipamento e ON o.idEquipamento = e.idEquipamento WHERE o.idEquipamento IS NULL;"
            resultado = cls.__banco.buscarTodos(query)
            
            logger_model.info("[BUSCA] Equipamentos sem reserva encontrados: %d", len(resultado))
            return resultado
        except Exception as e:
            logger_model.error("[BUSCA] Erro ao buscar equipamentos sem reserva. Erro: %s", e)
            return []
        finally:
            cls.__banco.desconectar()
            logger_model.debug("[BUSCA] Conexão com o banco encerrada.")

    # =================== Retorna Todos os Equipamentos ===================
    @classmethod
    def retorna_todos_equipamentos(cls):
        try:
            logger_model.info("[BUSCA] Iniciando busca de todos os equipamentos.")
            cls.__banco.conectar()
            query = "SELECT idEquipamento, nome FROM equipamento"
            resultado = cls.__banco.buscarTodos(query)
            
            logger_model.info("[BUSCA] Total de equipamentos encontrados: %d", len(resultado))
            return resultado
        except Exception as e:
            logger_model.error("[BUSCA] Erro ao buscar todos os equipamentos. Erro: %s", e)
            return []
        finally:
            cls.__banco.desconectar()
            logger_model.debug("[BUSCA] Conexão com o banco encerrada.")

    # =================== Retorna Sala do Equipamento ===================
    @classmethod
    def retorna_sala_equipamento(cls):
        try:
            logger_model.info("[BUSCA] Iniciando busca das salas dos equipamentos.")
            cls.__banco.conectar()
            
            query = """
                SELECT e.nome AS nomeEquipamento, e.marca, r.idSala, s.nome AS nomeSala 
                FROM equipamento e 
                INNER JOIN ocupado o ON e.idEquipamento = o.idEquipamento 
                INNER JOIN reserva r ON o.idReserva = r.idReserva 
                INNER JOIN sala s ON r.idSala = s.idSala
            """
            
            resultado = cls.__banco.buscarTodos(query)
            
            logger_model.info("[BUSCA] Total de registros encontrados: %d", len(resultado))
            return resultado
        except Exception as e:
            logger_model.error(f"[BUSCA] Erro ao buscar sala dos equipamentos: {e}")
            return []
        finally:
            cls.__banco.desconectar()
            logger_model.debug("[BUSCA] Conexão com o banco encerrada.")

    # =================== Retorna Nome, Quantidade, Sala e Docente ===================
    @classmethod
    def retorna_nome_quantidade_sala_docente_equipamento(cls):
        try:
            logger_model.info("[BUSCA] Iniciando busca de nome, quantidade, sala e docente dos equipamentos.")
            cls.__banco.conectar()
            
            query = """
                SELECT e.nome AS nomeEquipamento, r.idPessoa, r.idSala, p.nome AS nomePessoa, s.nome AS nomeSala 
                FROM equipamento e 
                INNER JOIN ocupado o ON e.idEquipamento = o.idEquipamento 
                INNER JOIN reserva r ON o.idReserva = r.idReserva 
                INNER JOIN sala s ON r.idSala = s.idSala 
                INNER JOIN pessoa p ON r.idPessoa = p.idPessoa
            """
            
            resultado = cls.__banco.buscarTodos(query)
            
            logger_model.info("[BUSCA] Total de registros encontrados: %d", len(resultado))
            return resultado
        except Exception as e:
            logger_model.error(f"[BUSCA] Erro ao buscar nome, quantidade, sala e docente dos equipamentos: {e}")
            return []
        finally:
            cls.__banco.desconectar()
            logger_model.debug("[BUSCA] Conexão com o banco encerrada.")

    # =================== Deletar Equipamento ===================
    @classmethod
    def deletar(cls, idEquipamento):
        try:
            logger_model.warning("[DELECAO] Tentando deletar equipamento com ID: %s", idEquipamento)
            cls.__banco.conectar()
            
            query = "DELETE FROM equipamento WHERE idEquipamento = %s"
            parametro = [idEquipamento]
            
            resultado = cls.__banco.alterarDados(query, parametro)
            
            if resultado.rowcount:
                logger_model.success("[DELECAO] Equipamento com ID %s deletado com sucesso.", idEquipamento)
            else:
                logger_model.warning("[DELECAO] Nenhum equipamento encontrado para deletar com ID %s.", idEquipamento)
            
            return bool(resultado.rowcount)
        except Exception as e:
            logger_model.error(f"[DELECAO] Erro ao deletar equipamento com ID {idEquipamento}: {e}")
            return False
        finally:
            cls.__banco.desconectar()
            logger_model.debug("[DELECAO] Conexão com o banco encerrada.")

    # =================== Atualizar Equipamento ===================
    @classmethod
    def atualizar(cls, idArea, nome, marca, quantidade, idEquipamento):
        try:
            logger_model.info("[ATUALIZACAO] Tentando atualizar equipamento com ID %s. Novo nome: %s", idEquipamento, nome)
            cls.__banco.conectar()
            
            query = "UPDATE equipamento SET `idArea`= %s, `nome`= %s, `marca`= %s, `quantidade`= %s WHERE idEquipamento = %s"
            parametro = [idArea, nome, marca, quantidade, idEquipamento]
            
            resultado = cls.__banco.alterarDados(query, parametro)
            
            if resultado.rowcount:
                logger_model.success("[ATUALIZACAO] Equipamento ID %s atualizado com sucesso.", idEquipamento)
            else:
                logger_model.warning("[ATUALIZACAO] Nenhuma alteração realizada para o equipamento ID %s.", idEquipamento)
            
            return bool(resultado.rowcount)
        except Exception as e:
            logger_model.error(f"[ATUALIZACAO] Erro ao atualizar equipamento com ID {idEquipamento}: {e}")
            return False
        finally:
            cls.__banco.desconectar()
            logger_model.debug("[ATUALIZACAO] Conexão com o banco encerrada.")

    # =================== Buscar ID ===================
    @classmethod
    def pesquisar_id(cls, idEquipamento):
        try:
            logger_model.info("[BUSCA ID] Iniciando busca do equipamento com ID %s", idEquipamento)
            cls.__banco.conectar()
            
            query = "SELECT * FROM equipamento WHERE idEquipamento = %s"
            resultado = cls.__banco.buscar(query, (idEquipamento,))
            
            if resultado:
                logger_model.success("[BUSCA ID] Equipamento encontrado com ID %s.", idEquipamento)
            else:
                logger_model.warning("[BUSCA ID] Nenhum equipamento encontrado com ID %s.", idEquipamento)
            
            return resultado
        except Exception as e:
            logger_model.error(f"[BUSCA ID] Erro ao pesquisar equipamento com ID {idEquipamento}: {e}")
            return None
        finally:
            cls.__banco.desconectar()
            logger_model.debug("[BUSCA ID] Conexão com o banco encerrada.")

if __name__ == "__main__":
    pass
