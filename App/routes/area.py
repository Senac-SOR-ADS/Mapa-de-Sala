from flask import render_template, Blueprint
from App.routes.login import login_required

# Definindo o blueprint
area_route = Blueprint('area', __name__, template_folder='templates')

@area_route.route("/", methods=['GET', 'POST'])
@login_required
def area():
    return render_template('area.html')

@area_route.route("/cadastrar", methods=['GET', 'POST'])
@login_required
def cadastrarArea():
    return render_template('cadastrarArea.html')
