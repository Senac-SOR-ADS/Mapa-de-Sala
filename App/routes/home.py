from flask import render_template, Blueprint
from App.routes.auth.autenticar import login_auth
from App.controllerWeb.login import pegar_acesso
from App.routes.utils import processar_mensagem

# Definindo o blueprint para a rota de home
home_route = Blueprint('home_route', __name__, template_folder='templates/Home/')

@home_route.route('/', methods=['GET'])
@home_route.route('/home', methods=['GET'])
@login_auth
def home():
    """Rota para a página inicial, protegida por autenticação."""
    try:
        valores = pegar_acesso()
        return render_template('/Home/home.html', usuario=valores)
    except Exception as e:
        processar_mensagem(mensagem=f"Erro ao acessar a página inicial: {str(e)}", nivel="ERROR", tipo_flash="danger")
        return render_template('/Error/error500.html'), 500

@home_route.app_errorhandler(404)
def page_not_found(error):
    """Tratamento de erro 404: Página não encontrada."""
    processar_mensagem(mensagem="Página não encontrada. Verifique o URL.", nivel="INFO", tipo_flash="danger")
    return render_template('/Error/error404.html'), 404
