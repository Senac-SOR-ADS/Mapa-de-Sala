from flask import render_template, Blueprint, request, flash, redirect, url_for
from App.routes.auth.autenticar import login_auth
from App.controller.area import cadastroDeArea, listarAreas

# Definindo o blueprint
area_route = Blueprint('area_route', __name__, template_folder='templates/Areas/')

@area_route.route("/", methods=['GET', 'POST'])
@login_auth
def listarArea():
    try:
        valores = listarAreas()
    except Exception as e:
        flash('Erro ao listar as áreas: {}'.format(str(e)), 'danger')
        valores = []

    return render_template('/Areas/listar.html', valores=valores)

@area_route.route("/cadastrar", methods=['GET', 'POST'])
@login_auth
def cadastrarArea():
    if request.method == 'POST':
        try:
            if request.is_json:
                dados = request.get_json()
                print('Dados recebidos (JSON):', dados)
            else:
                dados = request.form
                print('Dados recebidos (Formulário):', dados)

            # Captura os campos do formulário
            nomeArea = dados.get('nomeArea')

            # Cadastrando a área
            resultado = cadastroDeArea(nomeArea)
            flash('Área cadastrada com sucesso!', 'success')
            return redirect(url_for('area_route.cadastrarArea'))
        except Exception as e:
            flash('Erro ao cadastrar a área: {}'.format(str(e)), 'danger')

    return render_template('/Areas/cadastrar.html')

@area_route.route('/editar/<int:id>', methods=['GET'])
@login_auth
def editarArea():
    return render_template('/Areas/editar.html')
