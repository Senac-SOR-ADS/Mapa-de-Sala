import logging
import sys
from flask import Flask
from App.routes.routes import routes
from datetime import timedelta
from os import urandom
from App.model.conexao import ConexaoBD

# Inicializa a aplicação Flask
app = Flask(__name__)

app.register_blueprint(routes)

# Configurações da chave secreta e sessão
app.secret_key = urandom(12)
app.permanent_session_lifetime = timedelta(minutes=10)
app.session_refresh_each_request = True

# Configuração básica do logging
logging.basicConfig(level=logging.DEBUG)

# Verificando o acesso ao template
def check_template_access(app):
    """Verifica se o template 'home.html' está acessível."""
    try:
        app.jinja_env.get_template('home.html')
        logging.debug(" Template 'home.html' encontrado.")
    except Exception as e:
        logging.error(f" Erro ao encontrar template: {e}")


check_template_access(app)

# Conectando ao banco de dados
bd = ConexaoBD()
if bd.conectar():
    logging.info(" Conexão ao banco de dados bem-sucedida!")
    app.run(debug=True)

else:
    logging.error(" Erro ao conectar ao banco de dados.")
    sys.exit()