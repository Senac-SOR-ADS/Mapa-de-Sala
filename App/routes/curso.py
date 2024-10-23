from flask import render_template, Blueprint, request, flash, redirect, url_for
from App.routes.login import login_required
from App.controller import curso
from App.controller.area import listarAreas

# Definindo o blueprint
curso_route = Blueprint('curso_route', __name__, template_folder='templates/Cursos/')

@curso_route.route("/", methods=['GET', 'POST'])
@login_required
def listarCurso():
    try:
        valores = curso.listarCursos()
    except Exception as e:
        flash(f'Erro ao listar Cursos: {str(e)}', 'danger')
        valores = []
    return render_template('/Cursos/listar.html', valores=valores)

@curso_route.route("/cadastrar", methods=['GET', 'POST'])
@login_required
def cadastrarCurso():
    if request.method == 'POST':
        try:
            if request.is_json:
                dados = request.get_json()
                print('Dados recebidos (JSON):', dados)  
            else:
                dados = request.form
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
                return

            # Cadastrando o curso
            resultado = curso.cadastrarCurso(area, nome, oferta, periodo, carga, horas, alunos)
            flash('Curso cadastrado com sucesso!', 'success')
            return redirect(url_for('curso_route.cadastrarCurso'))
        except Exception as e:
            flash(f'Erro ao cadastrar o Curso: {str(e)}', 'danger')
 
    return render_template('/Cursos/cadastrar.html', valores=listarAreas())
    
@curso_route.route('/editar/<int:id>', methods=['GET'])
@login_required
def EditarCurso():
    return render_template('/Cursos/editar.html')