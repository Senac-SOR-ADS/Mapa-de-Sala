from flask import render_template, Blueprint, request, redirect, url_for
from App.routes.auth.autenticar import admin_auth, admin_suporte_auth
from App.controllerWeb.area import cadastroDeArea, listarAreas, buscarAreaId, atualizarArea, removerArea
from App.routes.utils import processar_mensagem, processar_resultado, processar_paginacao, processar_validacao, renderizar_com_mensagem

area_route = Blueprint('area_route', __name__, template_folder='templates/Areas/')

CAMPOS_AREA = ['nome']
VALIDACOES = {'nome': lambda nome: True if 3 <= len(nome) <= 100 and nome.replace(' ', '').isalnum() else "Nome da área deve ter entre 3 e 100 caracteres e ser alfanumérico."}

def processar_dados(dados: dict) -> dict: 
    return {'nome': dados.get('nomeArea', '').strip().title() if dados.get('nomeArea') else ''}

def validar(dados: dict) -> bool: 
    return processar_validacao(processar_dados(dados), tipo="obrigatorio", validacoes_adicionais=VALIDACOES)

# =================== Listar Áreas ===================
@area_route.route("/", methods=['GET'])
@admin_suporte_auth
def listar_Area():
    page, per_page, search_query = request.args.get('page', 1, type=int), 10, request.args.get('search', '', type=str)
    try:
        all_areas = listarAreas(search_query)
        if "error" in all_areas:
            return renderizar_com_mensagem('Areas/listar.html', {'search_query': search_query}, all_areas["error"], "ERROR", "danger")
        areas_paginated, total_items, total_pages, current_page, has_next, has_prev = processar_paginacao(list(all_areas.items()), page, per_page)
    except Exception as e:
        processar_mensagem(mensagem="Erro ao listar áreas: %s" % str(e), nivel="ERROR", tipo_flash="danger")
        return renderizar_com_mensagem('Areas/listar.html', {'search_query': search_query}, "Erro ao listar áreas. Tente novamente mais tarde, ou verifique a conexão.", "ERROR", "danger")
    return render_template('Areas/listar.html', valores=areas_paginated, total_items=total_items, total_pages=total_pages, page=current_page, per_page=per_page, search_query=search_query, has_next=has_next, has_prev=has_prev)

# =================== Cadastrar Área ===================
@area_route.route("/cadastrar", methods=['GET', 'POST'])
@admin_suporte_auth
def cadastrar_Area():
    if request.method == 'POST':
        dados = request.form.to_dict()
        if not validar(dados): 
            return renderizar_com_mensagem('Areas/cadastrar.html', {}, "Campos obrigatórios incorretos. Verifique os dados e tente novamente.", "ERROR", "danger")
        dados_processados = processar_dados(dados)
        try:
            result = cadastroDeArea(*dados_processados.values())
            if processar_resultado(result, f"Área {dados_processados['nome']} cadastrada com sucesso!", "Erro ao cadastrar a área. Verifique os dados e tente novamente.") :
                return redirect(url_for('area_route.listar_Area'))
        except Exception as e:
            processar_mensagem(mensagem="Erro ao cadastrar área: %s" % str(e), nivel="ERROR", tipo_flash="danger")
            return renderizar_com_mensagem('Areas/cadastrar.html', {}, "Erro ao cadastrar a área. Tente novamente mais tarde.", "ERROR", "danger")
    return render_template('Areas/cadastrar.html')

# =================== Editar Área ===================
@area_route.route('/editar/<int:id>', methods=['GET', 'POST'])
@admin_suporte_auth
def editar_Area(id):
    area = buscarAreaId(id)
    if not area or 'error' in area:
        processar_mensagem(mensagem="Área com ID %s não encontrada. Verifique o ID e tente novamente." % id, nivel="WARNING", tipo_flash="warning")
        return redirect(url_for('area_route.listar_Area'))
    if request.method == 'POST':
        dados = request.form.to_dict()
        if not validar(dados):
            return render_template('Areas/editar.html', area=area)
        dados_processados = processar_dados(dados)
        try:
            result = atualizarArea(id, **dados_processados)
            if result.get("success"):
                processar_mensagem(mensagem="Área %s com ID %s atualizada com sucesso!" % (dados_processados['nome'], id), nivel="INFO", tipo_flash="success")
                return redirect(url_for('area_route.listar_Area'))
            else:
                processar_mensagem(mensagem=result.get("error", "Erro ao atualizar a área. Tente novamente mais tarde."), nivel="ERROR", tipo_flash="danger")
        except Exception as e:
            processar_mensagem(mensagem="Erro ao editar área com ID %s: %s" % (id, str(e)), nivel="ERROR", tipo_flash="danger")
    return render_template('Areas/editar.html', area=area)

# =================== Remover Área ===================
@area_route.route('/remover/<int:id>', methods=['GET'])
@admin_auth
def remover_Area(id):
    try:
        area = buscarAreaId(id)
        if "error" in area:
            return renderizar_com_mensagem('Areas/listar.html', {}, "Erro ao buscar a área com ID %s: %s. Verifique o ID e tente novamente." % (id, area['error']), "ERROR", "danger")
        if processar_resultado(removerArea(id), success_message="Área com ID %s removida com sucesso!" % id):
            return redirect(url_for('area_route.listar_Area'))
    except Exception as e:
        processar_mensagem(mensagem="Erro ao remover área: %s. Verifique o ID e tente novamente." % str(e), nivel="ERROR", tipo_flash="danger", contexto_extra={'id': id})
    return redirect(url_for('area_route.listar_Area'))
