import logging
from App import app
from model.conexao import ConexaoBD

# Configuração básica do logging
logging.basicConfig(level=logging.DEBUG)

def check_template_access(app):
    """Verifica se o template 'home.html' está acessível."""
    try:
        app.jinja_env.get_template('home.html')
        logging.debug(" Template 'home.html' encontrado.")
    except Exception as e:
        logging.error(f" Erro ao encontrar template: {e}")

    # Conectando ao banco de dados
    bd = ConexaoBD()
    if bd.conectar():
        logging.info(" Conexão ao banco de dados bem-sucedida!")
    else:
        logging.error(" Erro ao conectar ao banco de dados.")

    # Verificando o acesso ao template
    check_template_access(app)

    # Executando a aplicação
    app.run(debug=True)
