from flask import Flask
from App.routes.auth.config import Config
from App.model.conexao import ConexaoBD
from App.routes.register import register_routes, check_template_access
from App.routes.logger_setup import logger
from socket import gethostbyname, gethostname
import sys

# Código de saída para falha na conexão
EXIT_CODE_CONNECTION_ERROR = 1

# Inicializa a aplicação Flask com as configurações definidas
app = Flask(__name__)
app.config.from_object(Config)

# Verifica se o template específico está acessível
check_template_access(app)

# Registra todas as rotas configuradas na aplicação
register_routes(app)

# Conecta ao banco de dados
bd = ConexaoBD()
if bd.conectar():
    logger.info("Conexão ao banco de dados estabelecida com sucesso.")

    # Obtém o endereço IP local do servidor
    ip_local = gethostbyname(gethostname())
    logger.info(f"Iniciando o servidor no endereço IP: {ip_local}")

    # Inicia o servidor Flask
    app.run(host=ip_local, debug=False)
else:
    logger.critical("Falha ao conectar ao banco de dados.")
    sys.exit(1)

