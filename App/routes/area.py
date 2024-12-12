from flask import render_template, Blueprint, request, flash, redirect, url_for
from App.routes.auth.autenticar import login_auth
from App.controller.area import cadastroDeArea, listarAreas, buscarAreaId, atualizarArea, removerArea

# Definindo o blueprint
area_route = Blueprint('area_route', __name__, template_folder='templates/Areas/')

# =================== Listar ===================
@area_route.route("/", methods=['GET'])
@login_auth
def listar_Area():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    search_query = request.args.get('search', '', type=str)

    try:
        all_areas = listarAreas(search_query)
        if not isinstance(all_areas, dict):
            raise ValueError("Esperava um dicionário de áreas")
        
        area_list = [(key, value) for key, value in all_areas.items()]
        total_items = len(area_list)
        start = (page - 1) * per_page
        end = start + per_page
        areas_paginated = area_list[start:end]

    except Exception as e:
        flash(f'Erro ao listar áreas: {str(e)}', 'danger')
        return render_template('Areas/listar.html', valores=[], total_items=0, page=1, per_page=per_page, search_query=search_query)
    
    return render_template('Areas/listar.html', valores=areas_paginated, total_items=total_items, page=page, per_page=per_page, search_query=search_query)

# =================== Cadastrar ===================
@area_route.route("/cadastrar", methods=['GET', 'POST'])
@login_auth
def cadastrar_Area():
    if request.method == 'POST':
        dados = request.form
        nomeArea = dados.get('nomeArea')

        if not nomeArea:
            flash('O campo nome da área é obrigatório.', 'danger')
            return render_template('Areas/cadastrar.html')

        try:
            if cadastroDeArea(nomeArea):
                flash('Área cadastrada com sucesso!', 'success')
                return redirect(url_for('area_route.listar_Area'))
            else:
                flash('Erro ao cadastrar a área.', 'danger')
        except Exception as e:
            flash(f'Erro ao cadastrar a área: {str(e)}', 'danger')

    return render_template('Areas/cadastrar.html')

# =================== Editar ===================
@area_route.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_auth
def editar_Area(id):
    area = buscarAreaId(id)

    if request.method == 'GET':
        if 'error' in area:
            flash(area['error'], 'danger')
            return redirect(url_for('area_route.listar_Area'))
        return render_template('Areas/editar.html', area=area)

    if request.method == 'POST':
        dados = request.form
        nomeArea = dados.get('nomeArea')

        if not nomeArea:
            flash('O campo nome da área é obrigatório.', 'danger')
            return render_template('Areas/editar.html', area=area)

        try:
            if atualizarArea(id, nomeArea):
                flash('Área atualizada com sucesso!', 'success')
                return redirect(url_for('area_route.listar_Area'))
            else:
                flash('Erro ao atualizar a área.', 'danger')
        except Exception as e:
            flash(f'Erro ao atualizar a área: {str(e)}', 'danger')
    
    return render_template('Areas/editar.html', area=area)

# =================== Remover ===================
@area_route.route('/remover/<int:id>', methods=['GET'])
@login_auth
def remover_Area(id):
    try:
        if removerArea(id):
            flash('Área removida com sucesso!', 'success')
        else:
            flash('Erro ao remover a área.', 'danger')
    except Exception as e:
        flash(f'Erro ao remover a área: {str(e)}', 'danger')

    return redirect(url_for('area_route.listar_Area'))
