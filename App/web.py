from flask import Flask
from App.routes.auth.config import Config
from App.model.conexao import ConexaoBD
from App.routes.register import register_routes, check_template_access
from App.routes.logger_setup import logger
from socket import gethostbyname, gethostname
import sys, platform

# Código de saída para falha na conexão
EXIT_CODE_CONNECTION_ERROR = 1

# Inicializa a aplicação Flask com as configurações definidas
app = Flask(__name__)
app.config.from_object(Config)

# Verifica se o template específico está acessível
check_template_access(app)

# Registra todas as rotas configuradas na aplicação
register_routes(app)

# Inicializa e conecta ao banco de dados
bd = ConexaoBD()
if bd.conectar():
    logger.info("Conexão ao banco de dados estabelecida com sucesso.")

    # Detecta o sistema operacional
    sistema = platform.system()
    
    if sistema == 'Windows':
        # usa o endereço IP local para rodar o servidor
        ip_local = gethostbyname(gethostname())
        logger.info(f"Sistema operacional detectado: Windows")
        logger.info(f"Iniciando o servidor no endereço IP: {ip_local}")
        app.run(host=ip_local, debug=True)
        
    elif sistema == 'Darwin':
        logger.info("Sistema operacional detectado: macOS")
        app.run(debug=True)

else:
    logger.critical("Falha ao conectar ao banco de dados.")
    sys.exit(EXIT_CODE_CONNECTION_ERROR)
