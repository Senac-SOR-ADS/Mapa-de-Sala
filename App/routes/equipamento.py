from flask import render_template, Blueprint, request, flash, redirect, url_for
from App.routes.auth.autenticar import login_auth
from App.controller.equipamento import cadastrarEquipamento, listarEquipamentos, buscarEquipamentoId, atualizarEquipamento, removerEquipamento
from App.controller.area import listarAreas

# Definindo o blueprint
equipamento_route = Blueprint('equipamento_route', __name__, template_folder='templates/Equipamentos/')

# =================== listar ===================
@equipamento_route.route("/", methods=['GET'])
@login_auth
def listar_Equipamento():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    search_query = request.args.get('search', '', type=str)

    try:
        all_equipments = listarEquipamentos(search_query)
        if not isinstance(all_equipments, dict):
            raise ValueError("Esperava um dicionário de equipamentos")

        equipment_list = [(key, value) for key, value in all_equipments.items()]
        total_items = len(equipment_list)
        start = (page - 1) * per_page
        end = start + per_page
        equipamentos_paginated = equipment_list[start:end]

    except Exception as e:
        flash(f'Erro ao listar equipamentos: {str(e)}', 'danger')
        return render_template('Equipamentos/listar.html', valores=[], total_items=0, page=1, per_page=per_page, search_query=search_query)
    
    return render_template('Equipamentos/listar.html', valores=equipamentos_paginated, total_items=total_items, page=page, per_page=per_page, search_query=search_query)

# =================== cadastrar ===================
@equipamento_route.route("/cadastrar", methods=['GET', 'POST'])
@login_auth
def cadastrar_Equipamento():
    areas = listarAreas()

    if request.method == 'POST':
        dados = request.form
        nome = dados.get('nome')
        descricao = dados.get('descricao')
        area_id = dados.get('area_id')

        if not all([nome, descricao, area_id]):
            flash('Todos os campos são obrigatórios.', 'danger')
            return render_template('Equipamentos/cadastrar.html', areas=areas)

        try:
            if cadastrarEquipamento(nome, descricao, area_id):
                flash('Equipamento cadastrado com sucesso!', 'success')
                return redirect(url_for('equipamento_route.listar_Equipamento'))
            else:
                flash('Erro ao cadastrar equipamento.', 'danger')
        except Exception as e:
            flash(f'Erro ao cadastrar equipamento: {str(e)}', 'danger')
    return render_template('Equipamentos/cadastrar.html', areas=areas)

# =================== atualizar ===================
@equipamento_route.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_auth
def editar_Equipamento(id):
    equipamento = buscarEquipamentoId(id)
    areas = listarAreas()

    if request.method == 'GET':
        if 'error' in equipamento:
            flash(equipamento['error'], 'danger')
            return redirect(url_for('equipamento_route.listar_Equipamento'))
        return render_template('Equipamentos/editar.html', equipamento=equipamento, areas=areas)

    if request.method == 'POST':
        dados = request.form
        nome = dados.get('nome')
        descricao = dados.get('descricao')
        area_id = dados.get('area_id')

        if not all([nome, descricao, area_id]):
            flash('Todos os campos são obrigatórios.', 'danger')
            return render_template('Equipamentos/editar.html', equipamento=equipamento, areas=areas)

        try:
            if atualizarEquipamento(id, nome, descricao, area_id):
                flash('Equipamento atualizado com sucesso!', 'success')
                return redirect(url_for('equipamento_route.listar_Equipamento'))
            else:
                flash('Erro ao atualizar equipamento.', 'danger')
        except Exception as e:
            flash(f'Erro ao atualizar equipamento: {str(e)}', 'danger')
    return render_template('Equipamentos/editar.html', equipamento=equipamento, areas=areas)

# =================== remover ===================
@equipamento_route.route('/remover/<int:id>', methods=['GET'])
@login_auth
def remover_Equipamento(id):
    """Remove um equipamento do banco de dados pelo ID."""
    try:
        if removerEquipamento(id):
            flash('Equipamento removido com sucesso!', 'success')
        else:
            flash('Erro ao remover equipamento.', 'danger')
    except Exception as e:
        flash(f'Erro ao remover equipamento: {str(e)}', 'danger')

    return redirect(url_for('equipamento_route.listar_Equipamento'))
