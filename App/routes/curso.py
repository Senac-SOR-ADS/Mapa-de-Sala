from flask import render_template, Blueprint, request, flash, redirect, url_for
from App.routes.auth.autenticar import login_auth
from App.controller.curso import listarCursos, cadastrarCurso, buscarCursoId, atualizarCurso, removerCurso
from App.controller.area import listarAreas

# Definindo o blueprint
curso_route = Blueprint('curso_route', __name__, template_folder='templates/Cursos/')

# =================== listar ===================
@curso_route.route("/", methods=['GET'])
@login_auth
def listar_Curso():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    search_query = request.args.get('search', '', type=str)

    try:
        all_courses = listarCursos(search_query)
        if not isinstance(all_courses, dict):
            raise ValueError("Esperava um dicionário de cursos")

        course_list = [(key, value) for key, value in all_courses.items()]
        total_items = len(course_list)
        start = (page - 1) * per_page
        end = start + per_page
        cursos_paginated = course_list[start:end]

    except Exception as e:
        flash(f'Erro ao listar cursos: {str(e)}', 'danger')
        return render_template('Cursos/listar.html', valores=[], total_items=0, page=1, per_page=per_page, search_query=search_query)
    
    return render_template('Cursos/listar.html', valores=cursos_paginated, total_items=total_items, page=page, per_page=per_page, search_query=search_query)

# =================== cadastrar ===================
@curso_route.route("/cadastrar", methods=['GET', 'POST'])
@login_auth
def cadastrar_Curso():
    if request.method == 'POST':
        dados = {
            'area': request.form.get('area'),
            'nome': request.form.get('nome'),
            'oferta': request.form.get('oferta'),
            'periodo': request.form.get('periodo'),
            'carga': request.form.get('carga'),
            'horas': request.form.get('horas'),
            'alunos': request.form.get('alunos')
        }

        # Print para debug: mostra todos os dados recebidos do formulário
        print(f"Dados recebidos do formulário: {dados}")

        if not all(dados.values()):
            flash('Todos os campos são obrigatórios.', 'danger')
            return render_template('Cursos/cadastrar.html', valores=listarAreas())

        try:
            resultado = cadastrarCurso(dados['area'], list(dados.values()))

            if "success" in resultado:
                flash(resultado["success"], 'success')
                return redirect(url_for('curso_route.listar_Curso'))
            else:
                flash(resultado["error"], 'danger')
        except Exception as e:
            flash(f'Erro ao cadastrar curso: {str(e)}', 'danger')

    return render_template('Cursos/cadastrar.html', valores=listarAreas())

# =================== editar ===================
@curso_route.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_auth
def editar_Curso(id):
    curso = buscarCursoId(id)

    if request.method == 'GET':
        if 'error' in curso:
            flash(curso['error'], 'danger')
            return redirect(url_for('curso_route.listar_Curso'))
        return render_template('Cursos/editar.html', curso=curso)

    if request.method == 'POST':
        dados = request.form
        area = dados.get('area')
        nome = dados.get('nome')
        oferta = dados.get('oferta')
        periodo = dados.get('periodo')
        carga = dados.get('carga')
        horas = dados.get('horas')
        alunos = dados.get('alunos')

        if not all([area, nome, oferta, periodo, carga, horas, alunos]):
            flash('Todos os campos são obrigatórios.', 'danger')
            return render_template('Cursos/editar.html', curso=curso)

        try:
            if atualizarCurso(id, area, nome, oferta, periodo, carga, horas, alunos):
                flash('Curso atualizado com sucesso!', 'success')
                return redirect(url_for('curso_route.listar_Curso'))
            else:
                flash('Erro ao atualizar curso.', 'danger')
        except Exception as e:
            flash(f'Erro ao atualizar curso: {str(e)}', 'danger')

    return render_template('Cursos/editar.html', curso=curso)

# =================== remover ===================
@curso_route.route('/remover/<int:id>', methods=['GET'])
@login_auth
def remover_Curso(id):
    """Remove um curso do banco de dados pelo ID."""
    try:
        if removerCurso(id):
            flash('Curso removido com sucesso!', 'success')
        else:
            flash('Erro ao remover curso.', 'danger')
    except Exception as e:
        flash(f'Erro ao remover curso: {str(e)}', 'danger')

    return redirect(url_for('curso_route.listar_Curso'))
