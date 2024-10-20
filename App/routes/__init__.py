from flask import Blueprint, Flask
from .home import home_route
from .login import login_route
from .pessoa import pessoa_route
from .reserva import reserva_route
from .sala import sala_route
from .area import area_route
from .curso import curso_route
from .equipamento import equipamento_route
from .logger_setup import logger

# Registra todos os blueprints na aplicação Flask.
def register_routes(app: Flask) -> None:
    
    # Lista de blueprints e seus respectivos prefixos de URL
    blueprints = [
        (home_route, '/'),
        (login_route, '/login'),
        (pessoa_route, '/funcionario'),
        (reserva_route, '/reserva'),
        (sala_route, '/sala'),
        (area_route, '/area'),
        (curso_route, '/curso'),
        (equipamento_route, '/equipamento')
    ]

    # Registra cada blueprint na aplicação
    for blueprint, url_prefix in blueprints:
        try:
            app.register_blueprint(blueprint, url_prefix=url_prefix)
            logger.info(f"Blueprint registrado: {blueprint} com o prefixo: {url_prefix}")
        except Exception as e:
            logger.error(f"Erro ao registrar blueprint: {blueprint} com o prefixo: {url_prefix}. Erro: {e}", exc_info=True)

def check_template_access(app: Flask) -> None:
    try:
        app.jinja_env.get_template('home.html')
        logger.info("Template 'home.html' encontrado com sucesso.")
    except Exception as e:
        logger.error(f"Erro ao acessar o template 'home.html': {e}", exc_info=True)
