from flask import render_template, Blueprint, request, flash, redirect, url_for
from App.routes.auth.autenticar import login_auth
from App.controller.sala import listarSala, cadastrarSala, buscarSalaId, atualizarSala, removerSala

# Definindo o blueprint
sala_route = Blueprint('sala_route', __name__, template_folder='templates/Salas/')

# =================== Listar ===================
@sala_route.route("/", methods=['GET'])
@login_auth
def listar_Sala():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    search_query = request.args.get('search', '', type=str)

    try:
        all_rooms = listarSala(search_query)
        if not isinstance(all_rooms, dict):
            raise ValueError("Esperava um dicionário de salas")

        sala_list = [(key, value) for key, value in all_rooms.items()]
        total_items = len(sala_list)
        start = (page - 1) * per_page
        end = start + per_page
        salas_paginated = sala_list[start:end]

    except Exception as e:
        flash(f'Erro ao listar as salas: {str(e)}', 'danger')
        return render_template('Salas/listar.html', valores=[], total_items=0, page=1, per_page=per_page, search_query=search_query)

    return render_template('Salas/listar.html', valores=salas_paginated, total_items=total_items, page=page, per_page=per_page, search_query=search_query)

# =================== Cadastrar ===================
@sala_route.route("/cadastrar", methods=['GET', 'POST'])
@login_auth
def cadastrar_Sala():
    if request.method == 'POST':
        dados = request.form
        nome = dados.get('nome')
        tipo = dados.get('tipo')
        predio = dados.get('predio')
        equipamento = dados.get('equipamento')
        capacidade = dados.get('capacidade')
        feedback = dados.get('feedback')

        if not all([nome, tipo, predio, capacidade]):
            flash('Os campos Nome, Tipo, Prédio e Capacidade são obrigatórios.', 'danger')
            return render_template('Salas/cadastrar.html')

        try:
            if cadastrarSala(nome, tipo, predio, equipamento, capacidade, feedback):
                flash('Sala cadastrada com sucesso!', 'success')
                return redirect(url_for('sala_route.listar_Sala'))
            else:
                flash('Erro ao cadastrar a sala.', 'danger')
        except Exception as e:
            flash(f'Erro ao cadastrar a sala: {str(e)}', 'danger')

    return render_template('Salas/cadastrar.html')

# =================== Editar ===================
@sala_route.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_auth
def editar_Sala(id):
    sala = buscarSalaId(id)

    if request.method == 'GET':
        if 'error' in sala:
            flash(sala['error'], 'danger')
            return redirect(url_for('sala_route.listar_Sala'))
        return render_template('Salas/editar.html', sala=sala)

    if request.method == 'POST':
        dados = request.form
        nome = dados.get('nome')
        tipo = dados.get('tipo')
        predio = dados.get('predio')
        equipamento = dados.get('equipamento')
        capacidade = dados.get('capacidade')
        feedback = dados.get('feedback')

        if not all([nome, tipo, predio, capacidade]):
            flash('Os campos Nome, Tipo, Prédio e Capacidade são obrigatórios.', 'danger')
            return render_template('Salas/editar.html', sala=sala)

        try:
            if atualizarSala(id, nome, tipo, predio, equipamento, capacidade, feedback):
                flash('Sala atualizada com sucesso!', 'success')
                return redirect(url_for('sala_route.listar_Sala'))
            else:
                flash('Erro ao atualizar a sala.', 'danger')
        except Exception as e:
            flash(f'Erro ao atualizar a sala: {str(e)}', 'danger')

    return render_template('Salas/editar.html', sala=sala)

# =================== Remover ===================
@sala_route.route('/remover/<int:id>', methods=['GET'])
@login_auth
def remover_Sala(id):
    """Remove uma sala do banco de dados pelo ID."""
    try:
        if removerSala(id):
            flash('Sala removida com sucesso!', 'success')
        else:
            flash('Erro ao remover a sala.', 'danger')
    except Exception as e:
        flash(f'Erro ao remover a sala: {str(e)}', 'danger')

    return redirect(url_for('sala_route.listar_Sala'))
