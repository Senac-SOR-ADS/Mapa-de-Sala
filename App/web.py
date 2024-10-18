import logging
import sys
from flask import Flask
from datetime import timedelta
from os import urandom
from App.model.conexao import ConexaoBD
from App.routes import home, login, pessoa, reserva, sala, area, curso, equipamento

# Inicializa a aplicação Flask
app = Flask(__name__)

# Configurações de segurança e sessão
app.secret_key = urandom(24)
app.permanent_session_lifetime = timedelta(minutes=10)
app.session_refresh_each_request = True

# Configuração de logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Formato e saída do logging
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Lista de blueprints e seus respectivos prefixos
blueprints = [
    (home.home_route, '/'),
    (login.login_route, '/login'),
    (pessoa.pessoa_route, '/funcionario'),
    (reserva.reserva_route, '/reserva'),
    (sala.sala_route, '/sala'),
    (area.area_route, '/area'),
    (curso.curso_route, '/curso'),
    (equipamento.equipamento_route, '/equipamento')
]

# Registra os blueprints no app
for rota, prefixo in blueprints:
    app.register_blueprint(rota, url_prefix=prefixo)

# Função para verificar acesso ao template
def check_template_access(app):
    """Verifica se o template 'home.html' está acessível e loga a situação."""
    try:
        app.jinja_env.get_template('home.html')
        logger.debug("Template 'home.html' encontrado com sucesso.")
    except Exception as e:
        logger.error(f"Erro ao tentar acessar o template 'home.html': {e}")

# Executa a verificação de acesso ao template
check_template_access(app)

# Conectando ao banco de dados
bd = ConexaoBD()
if bd.conectar():
    logger.info("Conexão ao banco de dados estabelecida com sucesso.")
    from socket import gethostbyname, gethostname
    ip_local = gethostbyname(gethostname())
    app.run(host=ip_local, debug=True)
else:
    logger.error("Falha ao conectar ao banco de dados.")
    sys.exit(1)
