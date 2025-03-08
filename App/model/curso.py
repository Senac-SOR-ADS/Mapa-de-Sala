from App.model.conexao import ConexaoBD
from App.model.logger import logger_model

class Curso:
    __banco = ConexaoBD()

    def __init__(self, nome, oferta, periodo, cargaHoraria, horasDia, qtdAlunos) -> None:
        self.__id = None
        self.__nome = nome
        self.__oferta = oferta
        self.__periodo = periodo
        self.__cargaHoraria = cargaHoraria
        self.__horasDia = horasDia
        self.__qtdAlunos = qtdAlunos

    # =================== Getters ===================
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_oferta(self): return self.__oferta
    def get_periodo(self): return self.__periodo
    def get_cargaHoraria(self): return self.__cargaHoraria
    def get_horasDia(self): return self.__horasDia
    def get_qtdAlunos(self): return self.__qtdAlunos

    # =================== Setters ===================
    def __set_id(self, id): self.__id = id
    def set_nome(self, nome): self.__nome = nome
    def set_oferta(self, oferta): self.__oferta = oferta
    def set_periodo(self, periodo): self.__periodo = periodo
    def set_cargaHoraria(self, cargaHoraria): self.__cargaHoraria = cargaHoraria
    def set_horasDia(self, horasDia): self.__horasDia = horasDia
    def set_qtdAlunos(self, qtdAlunos): self.__qtdAlunos = qtdAlunos

    # =================== Cadastrar Curso ===================
    def cadastrar_curso(self, id_area):
        """Cadastra um curso associado a uma área"""
        logger_model.info("[CADASTRO] %s", self.__nome)
        query = """
            INSERT INTO curso (idArea, nome, oferta, periodo, cargaHoraria, horasDia, qtdAlunos)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        params = [id_area, self.__nome, self.__oferta, self.__periodo, self.__cargaHoraria, self.__horasDia, self.__qtdAlunos]
        
        try:
            self.__banco.conectar()
            resultado = self.__banco.alterarDados(query, params)
            if resultado:
                logger_model.success("[CADASTRO] Curso cadastrado com sucesso: %s", self.__nome)
                return True
        except Exception as e:
            logger_model.error("[CADASTRO] Erro ao cadastrar curso: %s (Área ID: %s). Erro: %s", self.__nome, id_area, e)
        finally:
            self.__banco.desconectar()
            logger_model.debug("[CADASTRO] Conexão com o banco encerrada.")

        return False
    
    # =================== Retornar Informações dos Cursos ===================
    @classmethod
    def retorna_info_cursos(cls) -> list:
        logger_model.debug("[BUSCA] Iniciando busca de todos os cursos.")
        cls.__banco.conectar()
        
        query = "SELECT * FROM curso"
        logger_model.info("[BUSCA] Executando query: %s", query)
        
        resultado = []
        try:
            resultado = cls.__banco.buscarTodos(query)
        except Exception as e:
            logger_model.error("[BUSCA] Erro ao buscar cursos. Erro: %s", e)
        finally:
            cls.__banco.desconectar()

        lista_cursos = []
        if resultado:
            for item in resultado:
                if item and len(item) > 7:
                    try:
                        curso = cls(item[2], item[3], item[4], item[5], item[6], item[7])
                        curso.__set_id(item[0])
                        lista_cursos.append(curso)
                    except Exception as e:
                        logger_model.error("[BUSCA] Erro ao processar curso. Erro: %s", e)
        
        logger_model.success("[BUSCA] Total de cursos encontrados: %d", len(lista_cursos))
        return lista_cursos
    
    # =================== Retornar Todos os Cursos ===================
    @classmethod
    def retorna_todos_cursos(cls):
        """Retorna os nomes de todos os cursos"""
        logger_model.debug("[BUSCA] Buscando todos os cursos.")
        query = "SELECT nome FROM curso"
        
        try:
            cls.__banco.conectar()
            resultado = cls.__banco.buscarTodos(query)
        except Exception as e:
            logger_model.error("[BUSCA] Erro ao buscar cursos. Erro: %s", e)
            resultado = []
        finally:
            cls.__banco.desconectar()
            logger_model.debug("[BUSCA] Conexão com o banco encerrada.")
        
        logger_model.success("[BUSCA] Total de cursos encontrados: %d", len(resultado))
        return resultado
    
    # =================== Retornar Cursos por Área ===================
    @classmethod
    def retorna_curso_area(cls, id_area):
        """Retorna todos os cursos de uma área específica"""
        logger_model.debug("[BUSCA] Buscando cursos da área ID: %s", id_area)
        query = "SELECT * FROM curso WHERE idArea = %s"
        
        try:
            cls.__banco.conectar()
            resultado = cls.__banco.buscarTodos(query, [id_area])
        except Exception as e:
            logger_model.error("[BUSCA] Erro ao buscar cursos da área ID: %s. Erro: %s", id_area, e)
            resultado = []
        finally:
            cls.__banco.desconectar()
            logger_model.debug("[BUSCA] Conexão com o banco encerrada.")
        
        return resultado
    
    # =================== Retornar Cursos por Período ===================
    @classmethod
    def retorna_curso_periodo(cls, periodo):
        """Retorna todos os cursos de um período específico"""
        logger_model.debug("[BUSCA] Buscando cursos do período: %s", periodo)
        query = "SELECT * FROM curso WHERE periodo = %s"
        
        try:
            cls.__banco.conectar()
            resultado = cls.__banco.buscarTodos(query, [periodo])
        except Exception as e:
            logger_model.error("[BUSCA] Erro ao buscar cursos do período: %s. Erro: %s", periodo, e)
            resultado = []
        finally:
            cls.__banco.desconectar()
            logger_model.debug("[BUSCA] Conexão com o banco encerrada.")
        
        return resultado
    
    # =================== Retornar Oferta e ID dos Cursos ===================
    @classmethod
    def retorna_ofertaId_cursos(cls):
        """Retorna os IDs e ofertas de todos os cursos"""
        logger_model.debug("[BUSCA] Buscando ID e oferta de todos os cursos.")
        query = "SELECT idCurso, oferta FROM curso"
        
        try:
            cls.__banco.conectar()
            resultado = cls.__banco.buscarTodos(query)
        except Exception as e:
            logger_model.error("[BUSCA] Erro ao buscar ID e oferta dos cursos. Erro: %s", e)
            resultado = []
        finally:
            cls.__banco.desconectar()
            logger_model.debug("[BUSCA] Conexão com o banco encerrada.")
        
        logger_model.success("[BUSCA] Total de registros encontrados: %d", len(resultado))
        return resultado
    
    # =================== Retornar Nome do Cursos ===================
    @classmethod
    def retorna_todos_nomes_cursos(cls):
        """Retorna os IDs e nomes de todos os cursos"""
        logger_model.debug("[BUSCA] Buscando Nome de todos os cursos.")
        query = "SELECT idCurso, nome FROM curso"
        
        try:
            cls.__banco.conectar()
            resultado = cls.__banco.buscarTodos(query)
        except Exception as e:
            logger_model.error("[BUSCA] Erro ao buscar nomes dos cursos. Erro: %s", e)
            resultado = []
        finally:
            cls.__banco.desconectar()
            logger_model.debug("[BUSCA] Conexão com o banco encerrada.")
        
        logger_model.success("[BUSCA] Total de registros encontrados: %d", len(resultado))
        return resultado
    
    # =================== Retornar Todas as Informações do Curso ===================
    @classmethod
    def retorna_todas_infos_curso(cls, idCurso):
        """Retorna todas as informações de um curso dado o ID"""
        logger_model.debug("[BUSCA ID] Buscando todas as informações do curso com ID: %s", idCurso)
        query = "SELECT * FROM curso WHERE idCurso = %s"
        
        try:
            cls.__banco.conectar()
            resultado = cls.__banco.buscar(query, [idCurso])
            
            if resultado:
                logger_model.success("[BUSCA ID] Informações do curso encontradas para ID: %s", idCurso)
            else:
                logger_model.warning("[BUSCA ID] Nenhum curso encontrado para ID: %s", idCurso)
        except Exception as e:
            logger_model.error("[BUSCA ID] Erro ao buscar informações do curso ID: %s. Erro: %s", idCurso, e)
            resultado = None
        finally:
            cls.__banco.desconectar()
            logger_model.debug("[BUSCA ID] Conexão com o banco encerrada.")
        
        return resultado

    # =================== Deletar Curso ===================
    @classmethod
    def deletar(cls, idCurso):
        """Deleta um curso com base no ID fornecido"""
        logger_model.warning("[DELECAO] Tentando deletar curso com ID: %s", idCurso)
        query = "DELETE FROM curso WHERE idCurso = %s"
        
        try:
            cls.__banco.conectar()
            resultado = cls.__banco.alterarDados(query, [idCurso])
            
            if resultado and resultado.rowcount:
                logger_model.success("[DELECAO] Curso deletado com sucesso. ID: %s", idCurso)
                return True
            else:
                logger_model.warning("[DELECAO] Nenhum curso encontrado para deletar com ID: %s", idCurso)
                return False
        except Exception as e:
            logger_model.critical("[DELECAO] Erro ao deletar curso ID: %s. Erro: %s", idCurso, e)
            return False
        finally:
            cls.__banco.desconectar()
            logger_model.debug("[DELECAO] Conexão com o banco encerrada.")
    
    # =================== Atualizar Curso ===================
    @classmethod
    def atualizar(cls, idCurso, idArea, nome, oferta, periodo, cargaHoraria, horasDia, qtdAlunos):
        logger_model.info("[ATUALIZACAO] Iniciando atualização do curso com ID: %s, novo nome: '%s'", idCurso, nome)
        
        query = """
            UPDATE curso
            SET idArea = %s, nome = %s, oferta = %s, periodo = %s, cargaHoraria = %s, horasDia = %s, qtdAlunos = %s
            WHERE idCurso = %s
        """
        params = [idArea, nome, oferta, periodo, cargaHoraria, horasDia, qtdAlunos, idCurso]

        try:
            cls.__banco.conectar()
            resultado = cls.__banco.alterarDados(query, params)
            
            if resultado and resultado.rowcount:
                logger_model.success("[ATUALIZACAO] Curso atualizado com sucesso. ID: %s", idCurso)
                return True
            else:
                logger_model.warning("[ATUALIZACAO] Nenhuma atualização realizada no curso. ID: %s", idCurso)
                return False
                    
        except Exception as e:
            logger_model.error("[ATUALIZACAO] Erro ao atualizar curso ID %s. Erro: %s", idCurso, e)
            return False
        
        finally:
            cls.__banco.desconectar()
            logger_model.debug("[ATUALIZACAO] Conexão com o banco encerrada.")

    # =================== Buscar ID ===================
    @classmethod
    def pesquisar_id(cls, idCurso):
        logger_model.info("[BUSCA ID] Pesquisando curso com ID %s", idCurso)
        try:
            cls.__banco.conectar()
            query = "SELECT * FROM curso WHERE idCurso = %s"
            resultado = cls.__banco.buscar(query, (idCurso,))
            
            if resultado:
                logger_model.success("[BUSCA ID] Curso encontrado com sucesso. ID: %s", idCurso)
            else:
                logger_model.warning("[BUSCA ID] Nenhum curso encontrado com ID: %s", idCurso)
            
        except Exception as e:
            logger_model.error("[BUSCA ID] Erro ao pesquisar curso ID %s. Erro: %s", idCurso, e)
            resultado = None
        
        finally:
            cls.__banco.desconectar()
            logger_model.debug("[BUSCA ID] Conexão com o banco encerrada.")
        
        return resultado

if __name__ == "__main__":
    pass
