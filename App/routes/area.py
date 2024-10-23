from flask import render_template, Blueprint, request, flash, redirect, url_for
from App.routes.login import login_required
from App.controller.area import cadastroDeArea, listarAreas

# Definindo o blueprint
area_route = Blueprint('area_route', __name__, template_folder='templates/Areas/')

@area_route.route("/", methods=['GET', 'POST'])
@login_required
def listarArea():
    try:
        valores = listarAreas()
    except Exception as e:
        flash(f'Erro ao listar Salas: {str(e)}', 'danger')
        valores = []

    return render_template('/Areas/listar.html', valores=valores)

@area_route.route("/cadastrar", methods=['GET', 'POST'])
@login_required
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
            flash('Area cadastrada com sucesso!', 'success')
            return redirect(url_for('area_route.cadastrarArea'))
        except Exception as e:
            flash(f'Erro ao cadastrar a Area: {str(e)}', 'danger')
 
    return render_template('/Areas/cadastrar.html')

@area_route.route('/editar/<int:id>', methods=['GET'])
@login_required
def editarArea():
    return render_template('/Areas/editar.html')