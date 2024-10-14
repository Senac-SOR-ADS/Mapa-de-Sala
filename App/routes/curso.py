from flask import render_template, Blueprint
from App.routes.login import login_required

# Definindo o blueprint
curso_route = Blueprint('curso_route', __name__, template_folder='templates')

@curso_route.route("/", methods=['GET', 'POST'])
@login_required
def curso():
    return render_template('curso.html')

@curso_route.route("/cadastrar", methods=['GET', 'POST'])
@login_required
def cadastrarCurso():
    return render_template('cadastrarCurso.html')

