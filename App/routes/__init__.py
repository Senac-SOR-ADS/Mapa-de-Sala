# Importação do logger e rotas
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

# Definição dos elementos acessíveis ao importar o pacote
__all__ = [
    "logger",
    "home_route",
    "funcionario_route",
    "reserva_route",
    "relatorio_route",
    "sala_route",
    "area_route",
    "curso_route",
    "equipamento_route",
    "login_route",
    "logout_route",
    "register_routes",
    "check_template_access",
]
