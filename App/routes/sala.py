from flask import render_template, Blueprint
from App.routes.login import login_required

# Definindo o blueprint
sala_route = Blueprint('sala_route', __name__, template_folder='templates')

@sala_route.route("/", methods=['GET', 'POST'])
@login_required
def sala():
    return render_template('sala.html')

@sala_route.route("/cadastrar", methods=['GET', 'POST'])
@login_required
def cadastrarSala():
    return render_template('cadastrarSala.html')