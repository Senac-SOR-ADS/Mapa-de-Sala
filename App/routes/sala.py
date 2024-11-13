from flask import render_template, Blueprint, request, flash, redirect, url_for
from App.routes.auth.autenticar import login_auth
from App.controller.sala import listarSala, cadastrarSala

# Definindo o blueprint
sala_route = Blueprint('sala_route', __name__, template_folder='templates/Salas/')

@sala_route.route("/", methods=['GET', 'POST'])
@login_auth
def listar_Sala():
    page = request.args.get('page', 1, type=int)
    per_page = 10

    try:
        all_rooms = listarSala()
        if not isinstance(all_rooms, dict):
            raise ValueError("Esperava um dicionário de salas")

        sala_list = [(key, value) for key, value in all_rooms.items()]

        total_items = len(sala_list)
        start = (page - 1) * per_page
        end = start + per_page
        salas_paginated = sala_list[start:end]

    except Exception as e:
        flash(f'Erro ao listar as salas: {str(e)}', 'danger')
        return render_template('/Salas/listar.html', valores=[], total_items=0, page=1, per_page=per_page)

    return render_template('/Salas/listar.html', valores=salas_paginated, total_items=total_items, page=page, per_page=per_page)

@sala_route.route("/cadastrar", methods=['GET', 'POST'])
@login_auth
def cadastrar_Sala():
    if request.method == 'POST':
        try:
            if request.is_json:
                dados = request.get_json()
                print('Dados recebidos (JSON):', dados)  
            else:
                dados = request.form
                print('Dados recebidos (Formulário):', dados)

            # Captura os campos do formulário
            nome = dados.get('nome')
            tipo = dados.get('tipo')
            predio = dados.get('predio')  
            equipamento = dados.get('equipamento')
            capacidade = dados.get('capacidade')
            feedback = dados.get('feedback')

            # Validação dos campos
            if not all([nome, tipo, predio, capacidade]):
                flash('Todos os campos (nome, tipo, prédio e capacidade) são obrigatórios.', 'danger')
                return render_template('/Salas/cadastrar.html')

            # Cadastrando a sala
            resultado = cadastrarSala(nome, tipo, predio, equipamento, capacidade, feedback)
            flash('Sala cadastrada com sucesso!', 'success')
            return redirect(url_for('sala_route.cadastrar_Sala'))
        except Exception as e:
            flash(f'Erro ao cadastrar a sala: {str(e)}', 'danger')
 
    return render_template('/Salas/cadastrar.html')

@sala_route.route('/editar/<int:id>', methods=['GET'])
@login_auth
def editarSala():
    return render_template('/Salas/editar.html')
