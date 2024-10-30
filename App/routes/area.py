from flask import render_template, Blueprint, request, flash, redirect, url_for
from App.routes.auth.autenticar import login_auth
from App.controller.area import cadastroDeArea, listarAreas

# Definindo o blueprint
area_route = Blueprint('area_route', __name__, template_folder='templates/Areas/')

@area_route.route("/", methods=['GET', 'POST'])
@login_auth
def listarArea():
    page = request.args.get('page', 1, type=int)
    per_page = 10

    try:
        allAreas = listarAreas()
        if not isinstance(allAreas, dict):
            raise ValueError("Esperava um dicionário de áreas")
        
        area_list = [(key, value) for key, value in allAreas.items()]

        total_items = len(area_list)
        start = (page - 1) * per_page
        end = start + per_page
        areas_paginated = area_list[start:end]

    except Exception as e:
        flash(f'Erro ao listar as áreas: {str(e)}', 'danger')
        return render_template('/Areas/listar.html', valores=[], total_items=0, page=1, per_page=per_page)
 
    return render_template('/Areas/listar.html', valores=areas_paginated, total_items=total_items, page=page, per_page=per_page)

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
