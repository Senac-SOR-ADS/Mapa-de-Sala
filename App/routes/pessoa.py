from flask import render_template, Blueprint, request, flash, jsonify
from App.routes.login import login_required
from App.controller.pessoa import cadastrarPessoa
import re

# Definindo o blueprint
pessoa_route = Blueprint('pessoa_route', __name__, template_folder='templates')

@pessoa_route.route("/", methods=['GET', 'POST'])
@login_required
def funcionario():
    return render_template('funcionario.html')

@pessoa_route.route("/cadastrar", methods=['GET', 'POST'])
@login_required
def cadastrarFuncionario():
    return render_template('cadastrarFuncionario.html')

