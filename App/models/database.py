import os
import logging
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Inicializar o SQLAlchemy
db = SQLAlchemy()

def testeConexao():
    """Verifica a conexão com o banco de dados."""
    try:
        db.session.execute(text('SELECT 1'))
        logger.info("Conexão com o banco de dados bem-sucedida.")
    except Exception as e:
        logger.error(f"Erro ao conectar-se ao banco de dados: {e}")
        raise

def buscar(query: str, param: dict = None):
    """Executa uma consulta e retorna um único resultado."""
    try:
        result = db.session.execute(text(query), param).fetchone()
        return result
    except Exception as e:
        logger.error(f"Erro ao buscar dados: {e} - Consulta: {query} - Parâmetros: {param}")
        return None

def buscarTodos(query: str, param: dict = None):
    """Executa uma consulta e retorna todos os resultados."""
    try:
        results = db.session.execute(text(query), param).fetchall()
        return results
    except Exception as e:
        logger.error(f"Erro ao buscar dados: {e} - Consulta: {query} - Parâmetros: {param}")
        return []

def alterarDados(query: str, param: dict = None):
    """Executa uma alteração no banco de dados."""
    try:
        db.session.execute(text(query), param)
        commit()
        logger.info("Dados alterados com sucesso.")
    except Exception as e:
        logger.error(f"Erro ao alterar dados: {e} - Consulta: {query} - Parâmetros: {param}")

def commit():
    """Confirma as alterações no banco de dados."""
    try:
        db.session.commit()
    except Exception as e:
        logger.error(f"Erro ao confirmar a transação: {e}")
        db.session.rollback()
