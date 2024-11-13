from flask import render_template, Blueprint, request, flash, redirect, url_for
from App.routes.auth.autenticar import login_auth
from App.controller.curso import listarCursos, cadastrarCurso
from App.controller.area import listarAreas

# Definindo o blueprint
curso_route = Blueprint('curso_route', __name__, template_folder='templates/Cursos/')

@curso_route.route("/", methods=['GET', 'POST'])
@login_auth
def listar_Curso():
    page = request.args.get('page', 1, type=int)
    per_page = 10

    try:
        all_courses = listarCursos()
        if not isinstance(all_courses, dict):
            raise ValueError("Esperava um dicionário de cursos")

        curso_list = [(key, value) for key, value in all_courses.items()]

        total_items = len(curso_list)
        start = (page - 1) * per_page
        end = start + per_page
        cursos_paginated = curso_list[start:end]

    except Exception as e:
        flash(f'Erro ao listar os cursos: {str(e)}', 'danger')
        return render_template('/Cursos/listar.html', valores=[], total_items=0, page=1, per_page=per_page)

    return render_template('/Cursos/listar.html', valores=cursos_paginated, total_items=total_items, page=page, per_page=per_page)

@curso_route.route("/cadastrar", methods=['GET', 'POST'])
@login_auth
def cadastrar_Curso():
    if request.method == 'POST':
        try:
            dados = request.form  # Captura os dados do formulário
            print('Dados recebidos (Formulário):', dados)

            # Captura os campos do formulário
            area = dados.get('area')
            nome = dados.get('nome')
            oferta = dados.get('oferta')
            periodo = dados.get('periodo')
            carga = dados.get('carga')
            horas = dados.get('horas')
            alunos = dados.get('alunos')

            # Validação dos campos
            if not all([area, nome, oferta, periodo, carga, horas, alunos]):
                flash('Todos os campos são obrigatórios.', 'danger')
                return redirect(url_for('curso_route.cadastrar_Curso'))

            # Cadastrando o curso
            resultado = cadastrarCurso(area, nome, oferta, periodo, carga, horas, alunos)
            if resultado:
                flash('Curso cadastrado com sucesso!', 'success')
            else:
                flash('Erro ao cadastrar o curso.', 'danger')
            return redirect(url_for('curso_route.cadastrar_Curso'))
        except Exception as e:
            flash('Erro ao cadastrar o curso: {}'.format(str(e)), 'danger')

    return render_template('/Cursos/cadastrar.html', valores=listarAreas())



@curso_route.route('/editar/<int:id>', methods=['GET'])
@login_auth
def EditarCurso():
    return render_template('/Cursos/editar.html')
