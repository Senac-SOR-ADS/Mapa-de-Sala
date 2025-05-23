from flask import render_template, Blueprint, request, redirect, url_for
from App.routes.auth.autenticar import admin_auth, admin_suporte_auth
from App.controllerWeb.curso import listarCursos, cadastrarCurso, buscarCursoId, atualizarCurso, removerCurso
from App.controllerWeb.area import listarAreas
from App.routes.utils import processar_mensagem, processar_resultado, processar_paginacao, processar_validacao, renderizar_com_mensagem

curso_route = Blueprint('curso_route', __name__, template_folder='templates/Cursos/')

# -------------------------- Funções Auxiliares ------------------------
CAMPOS_CURSO = ['area', 'nome', 'oferta', 'periodo', 'carga', 'horas', 'alunos']
VALIDACOES = {'nome': lambda nome: True if 3 <= len(nome) <= 100 and nome.replace(' ', '').isalnum() else "O nome do curso deve ter entre 3 e 100 caracteres e ser alfanumérico."}

def processar_dados(dados: dict) -> dict:
    return {campo: dados.get(campo, '').strip() if campo != 'nome' else dados.get(campo, '').strip().title() for campo in CAMPOS_CURSO}

def validar(dados: dict) -> bool:
    return processar_validacao(dados, tipo="obrigatorio", validacoes_adicionais=VALIDACOES)

# =================== Listagem de Cursos ===================
@curso_route.route("/", methods=['GET'])
@admin_suporte_auth
def listar_Curso():
    page, per_page, search_query = request.args.get('page', 1, type=int), 10, request.args.get('search', '', type=str)
    all_courses = listarCursos(search_query)
    if not isinstance(all_courses, dict):
        return renderizar_com_mensagem('Cursos/listar.html', {'valores': [], 'total_items': 0, 'page': 1, 'per_page': per_page, 'search_query': search_query}, 'Erro ao listar cursos. Tente novamente mais tarde. Se o problema persistir, verifique sua conexão com a internet.', "ERROR", "danger")
    course_list = list(all_courses.items())
    cursos_paginated, total_items, total_pages, current_page, has_next, has_prev = processar_paginacao(course_list, page, per_page)
    return render_template('Cursos/listar.html', valores=cursos_paginated, total_items=total_items, total_pages=total_pages, page=current_page, per_page=per_page, search_query=search_query, has_next=has_next, has_prev=has_prev)

# =================== Cadastro de Curso ===================
@curso_route.route("/cadastrar", methods=['GET', 'POST'])
@admin_suporte_auth
def cadastrar_Curso():
    if request.method == 'POST':
        dados = request.form.to_dict()
        if not validar(dados): 
            return renderizar_com_mensagem('Cursos/cadastrar.html', {'valores': listarAreas()}, 'Erro de validação. Verifique os campos obrigatórios e tente novamente.', "ERROR", "danger")
        dados_processados = processar_dados(dados)
        if 'error' in dados_processados:
            return renderizar_com_mensagem('Cursos/cadastrar.html', {'valores': listarAreas()}, dados_processados['error'], "ERROR", "danger")
        result = cadastrarCurso(dados_processados['area'], list(dados_processados.values()))
        if processar_resultado(result, f"Curso {dados['nome']} cadastrado com sucesso!", "Erro ao cadastrar o curso. Verifique os dados e tente novamente. Se o problema persistir, entre em contato com o suporte.") :
            return redirect(url_for('curso_route.listar_Curso'))
    return render_template('Cursos/cadastrar.html', valores=listarAreas())

# =================== Edição de Curso ===================
@curso_route.route('/editar/<int:id>', methods=['GET', 'POST'])
@admin_suporte_auth
def editar_Curso(id):
    curso = buscarCursoId(id)
    if not curso or 'error' in curso:
        return renderizar_com_mensagem('Cursos/editar.html', {}, 'Curso não encontrado. Verifique o ID e tente novamente. Se o erro continuar, certifique-se de que o ID está correto.', "WARNING", "warning")
    if request.method == 'POST':
        dados = request.form.to_dict()
        if not validar(dados): 
            return renderizar_com_mensagem('Cursos/editar.html', {'curso': curso, 'valores': listarAreas()}, 'Erro de validação. Verifique os campos obrigatórios e tente novamente.', "ERROR", "danger")
        dados_processados = processar_dados(dados)
        result = atualizarCurso(id, *list(dados_processados.values()))
        if processar_resultado(result, f"Curso {dados['nome']} com ID {id} atualizado com sucesso!", "Erro ao atualizar o curso. Verifique os dados e tente novamente. Caso o erro persista, entre em contato com o suporte.") :
            return redirect(url_for('curso_route.listar_Curso'))
    return render_template('Cursos/editar.html', curso=curso, valores=listarAreas())

# =================== Remoção de Curso ===================
@curso_route.route('/remover/<int:id>', methods=['GET'])
@admin_auth
def remover_Curso(id):
    try:
        result = removerCurso(id)
        if not processar_resultado(result, "Curso removido com sucesso!", "Erro ao remover o curso. Tente novamente mais tarde. Se o erro persistir, entre em contato com o suporte.") :
            raise Exception(f"Falha ao remover o curso com ID {id}.")
    except Exception as e:
        processar_mensagem(mensagem=f"Erro ao remover o curso: {str(e)}. Verifique se o ID está correto e tente novamente.", nivel="ERROR", tipo_flash="danger", contexto_extra={'id': id})
    return redirect(url_for('curso_route.listar_Curso'))
