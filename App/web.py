from flask import Flask
from socket import gethostbyname, gethostname
import sys, platform, time
from App.routes.auth.config import Config
from App.model.conexao import ConexaoBD
from App.routes.register import register_routes
from App.routes.auth.acesso import verificar_expiracao
from App.model.logger import logger

# Código de saída para falha na conexão
EXIT_CODE_CONNECTION_ERROR = 1

def identificar_sistema():
    """Identifica o sistema operacional e registra detalhes."""
    sistema = platform.system()
    versao = platform.version()
    arquitetura = platform.architecture()[0]
    detalhes = f"Sistema Operacional: {sistema}, Versão: {versao}, Arquitetura: {arquitetura}"
    
    logger.info(f"Sistema detectado: {detalhes}")
    return sistema, detalhes

# Inicializa a aplicação Flask
app = Flask(__name__)
app.config.from_object(Config)
register_routes(app)

@app.before_request
def before_request():
    verificar_expiracao()

# Inicializa e conecta ao banco de dados
bd = ConexaoBD()

start_time = time.time()
if not bd.conexao_valida:
    logger.warning("Tentando estabelecer conexão com o banco de dados...")
    bd.conectar()

if bd.conexao_valida:
    logger.info(f"Conexão ao banco de dados '{bd.nome_banco}' estabelecida com sucesso em {platform.node()} após {time.time() - start_time:.2f} segundos.")
else:
    logger.critical("Falha ao conectar ao banco de dados após múltiplas tentativas.")
    sys.exit(EXIT_CODE_CONNECTION_ERROR)

sistema, detalhes_sistema = identificar_sistema()

try:
    if sistema == 'Windows':
        ip_local = gethostbyname(gethostname())
        logger.info(f"Iniciando o servidor no endereço IP: {ip_local}", extra={"system": sistema, "ip": ip_local, "details": detalhes_sistema})
        app.run(host=ip_local, debug=Config.DEBUG)
    else:
        logger.info(f"Sistema operacional detectado: {sistema}")
        app.run(debug=Config.DEBUG)
except Exception as e:
    logger.critical(f"Erro inesperado ao iniciar o servidor: {str(e)}", exc_info=True)
    sys.exit(EXIT_CODE_CONNECTION_ERROR)
finally:
    bd.desconectar()
