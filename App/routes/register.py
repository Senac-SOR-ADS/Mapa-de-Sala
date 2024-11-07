from flask import Flask
from .logger_setup import logger

# Importa todas as rotas do sistema 
from .home import home_route
from .pessoa import funcionario_route
from .reserva import reserva_route
from .relatorios import relatorio_route
from .sala import sala_route
from .area import area_route
from .curso import curso_route
from .equipamento import equipamento_route
from .auth.login import login_route
from .auth.logout import logout_route

def register_routes(app: Flask) -> None:
    """
    Registra todos os blueprints na aplicação Flask.
    
    Args:
        app (Flask): A instância da aplicação Flask onde as rotas serão registradas.
    """
    blueprints = [
        (home_route, '/'),
        (login_route, '/login'),
        (logout_route, '/logout'),
        (funcionario_route, '/funcionario'),
        (reserva_route, '/reserva'),
        (relatorio_route, '/relatorio'),       
        (sala_route, '/sala'),
        (area_route, '/area'),
        (curso_route, '/curso'),
        (equipamento_route, '/equipamento')
    ]

    for blueprint, url_prefix in blueprints:
        try:
            app.register_blueprint(blueprint, url_prefix=url_prefix)
            logger.info(f"Blueprint registrado: {blueprint} com o prefixo: {url_prefix}")
        except Exception as e:
            logger.error(f"Erro ao registrar blueprint: {blueprint} com o prefixo: {url_prefix}. Erro: {e}", exc_info=True)

def check_template_access(app: Flask) -> None:
    """
    Verifica se o template 'home.html' está acessível no ambiente Jinja da aplicação.

    Args:
        app (Flask): A instância da aplicação Flask usada para acessar os templates.
    """
    try:
        app.jinja_env.get_template('/Home/home.html')
        logger.info("Template 'home.html' encontrado com sucesso.")
    except Exception as e:
        logger.error(f"Erro ao acessar o template 'home.html': {e}", exc_info=True)
