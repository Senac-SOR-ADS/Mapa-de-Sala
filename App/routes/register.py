from flask import Flask
from .logger_setup import logger
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
    
    success = False

    for blueprint, url_prefix in blueprints:
        blueprint_name = blueprint.name if hasattr(blueprint, 'name') else str(blueprint)
        try:
            app.register_blueprint(blueprint, url_prefix=url_prefix)
            success = True
        except Exception as e:
            logger.error(f"Erro ao registrar blueprint '{blueprint_name}' com o prefixo '{url_prefix}': {e}")
    
    # Registra uma única vez se algum blueprint foi registrado com sucesso
    if success:
        logger.info("Blueprints registrados com sucesso")
