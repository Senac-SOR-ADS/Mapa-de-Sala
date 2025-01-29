from flask import Flask
from App.routes.auth.config import Config
from App.model.conexao import ConexaoBD
from App.routes.register import register_routes
from App.routes.logger_setup import logger
from socket import gethostbyname, gethostname
from App.routes.auth.acesso import verificar_expiracao
import sys, platform

# Código de saída para falha na conexão
EXIT_CODE_CONNECTION_ERROR = 1

# Função para identificar o sistema operacional e coletar detalhes adicionais
def identificar_sistema():
    sistema = platform.system()
    versao = platform.version()
    arquitetura = platform.architecture()[0]
    detalhes = f"Sistema Operacional: {sistema}, Versão: {versao}, Arquitetura: {arquitetura}"
    
    # Log detalhado do sistema operacional
    logger.info(f"Sistema detectado: {detalhes}")
    return sistema, detalhes

# Inicializa a aplicação Flask com as configurações definidas
app = Flask(__name__)
app.config.from_object(Config)

# Registra todas as rotas configuradas na aplicação
register_routes(app)

# Função chamada antes de cada requisição
@app.before_request
def before_request():
    verificar_expiracao()

# Inicializa e conecta ao banco de dados
bd = ConexaoBD()
try:
    if bd.conectar():
        logger.info("Conexão ao banco de dados estabelecida com sucesso.")
        
        # Identifica e loga o sistema operacional
        sistema, detalhes_sistema = identificar_sistema()
        
        if sistema == 'Windows':
            # Usa o endereço IP local para rodar o servidor
            ip_local = gethostbyname(gethostname())
            logger.info(f"Iniciando o servidor no endereço IP: {ip_local}", extra={"system": sistema, "ip": ip_local, "details": detalhes_sistema})
            app.run(host=ip_local, debug=False)

        elif sistema == 'Darwin':
            logger.info("Sistema operacional detectado: macOS")
            app.run(debug=False)

        else:
            logger.info(f"Sistema operacional não identificado explicitamente: {sistema}")
            app.run(debug=False)

    else:
        logger.critical("Falha ao conectar ao banco de dados.")
        sys.exit(EXIT_CODE_CONNECTION_ERROR)

except Exception as e:
    logger.critical(f"Erro inesperado ao tentar conectar ao banco de dados: {str(e)}")
    sys.exit(EXIT_CODE_CONNECTION_ERROR)
