from flask import render_template, Blueprint, request, redirect, url_for
from App.routes.auth.autenticar import admin_auth, admin_suporte_auth
from App.controllerWeb.equipamento import cadastrarEquipamento, listarEquipamentos, buscarEquipamentoId, atualizarEquipamento, removerEquipamento
from App.controllerWeb.area import listarAreas
from App.routes.utils import processar_mensagem, processar_resultado, processar_paginacao, processar_validacao, renderizar_com_mensagem

equipamento_route = Blueprint('equipamento_route', __name__, template_folder='templates/Equipamentos/')

# -------------------------- Funções Auxiliares ------------------------
CAMPOS_EQUIPAMENTO = ['nome', 'marca', 'quantidade', 'idArea']
VALIDACOES = {
    'nome': lambda nome: True if 3 <= len(nome) <= 100 else "O nome do equipamento deve ter entre 3 e 100 caracteres.",
    'marca': lambda marca: True if marca else "A marca do equipamento não pode estar vazia.",
}

def processar_dados(dados: dict) -> dict:
    return {campo: dados.get(campo, '').strip() for campo in CAMPOS_EQUIPAMENTO}

def validar(dados: dict) -> bool:
    return processar_validacao(dados, tipo="obrigatorio", validacoes_adicionais=VALIDACOES)

# =================== Listar Equipamentos ===================
@equipamento_route.route("/", methods=['GET'])
@admin_suporte_auth
def listar_Equipamento():
    page, per_page, search_query = request.args.get('page', 1, type=int), 10, request.args.get('search', '', type=str)
    equipamentos_dict = listarEquipamentos(search_query)
    if not isinstance(equipamentos_dict, dict):
        processar_mensagem(mensagem="Erro ao listar equipamentos. Verifique a conexão ou os parâmetros de pesquisa.", nivel="ERROR", tipo_flash="danger")
        return renderizar_com_mensagem('Equipamentos/listar.html', {'valores': [], 'total_items': 0, 'page': 1, 'per_page': per_page, 'search_query': search_query}, 'Erro ao listar equipamentos.', "ERROR", "danger")
    equipment_list = list(equipamentos_dict.items())
    equipamentos_paginated, total_items, total_pages, current_page, has_next, has_prev = processar_paginacao(equipment_list, page, per_page)
    return render_template('Equipamentos/listar.html', valores=equipamentos_paginated, total_items=total_items, total_pages=total_pages, page=current_page, per_page=per_page, search_query=search_query, has_next=has_next, has_prev=has_prev)

# =================== Cadastrar Equipamento ===================
@equipamento_route.route("/cadastrar", methods=['GET', 'POST'])
@admin_suporte_auth
def cadastrar_Equipamento():
    if request.method == 'POST':
        dados = request.form.to_dict()
        if not validar(dados): 
            processar_mensagem(mensagem="Erro de validação. Verifique os campos obrigatórios.", nivel="ERROR", tipo_flash="danger")
            return render_template('Equipamentos/cadastrar.html', mensagem="Erro de validação. Verifique os campos obrigatórios.", valores=listarAreas())
        dados_processados = processar_dados(dados)
        resultado = cadastrarEquipamento(dados_processados['idArea'], dados_processados)
        if processar_resultado(resultado, f"Equipamento {dados['nome']} cadastrado com sucesso!", "Erro ao cadastrar equipamento. Verifique os dados e tente novamente."):
            return redirect(url_for('equipamento_route.listar_Equipamento'))
    return render_template('Equipamentos/cadastrar.html', valores=listarAreas())

# =================== Atualizar Equipamento ===================
@equipamento_route.route('/editar/<int:id>', methods=['GET', 'POST'])
@admin_suporte_auth
def editar_Equipamento(id):
    equipamento = buscarEquipamentoId(id)
    if not equipamento or 'error' in equipamento:
        processar_mensagem(mensagem=f"Equipamento com ID {id} não encontrado. Verifique o ID e tente novamente.", nivel="WARNING", tipo_flash="warning")
        return redirect(url_for('equipamento_route.listar_Equipamento'))
    if request.method == 'POST':
        dados = request.form.to_dict()
        if not validar(dados):
            return render_template('Equipamentos/editar.html', equipamento=equipamento, valores=listarAreas())
        dados_processados = processar_dados(dados)
        result = atualizarEquipamento(id, **dados_processados)
        if processar_resultado(result, f"Equipamento {dados['nome']} atualizado com sucesso!", "Erro ao atualizar equipamento. Verifique os dados e tente novamente."):
            return redirect(url_for('equipamento_route.listar_Equipamento'))
    return render_template('Equipamentos/editar.html', equipamento=equipamento, valores=listarAreas())

# =================== Remover Equipamento ===================
@equipamento_route.route('/remover/<int:id>', methods=['GET'])
@admin_auth
def remover_Equipamento(id):
    try:
        result = removerEquipamento(id)
        if not processar_resultado(result, f"Equipamento com ID {id} removido com sucesso!", f"Erro ao remover o equipamento com ID {id}. Verifique o ID e tente novamente."):
            raise Exception(f"Falha ao remover o equipamento com ID {id}.")
    except Exception as e:
        processar_mensagem(mensagem=f"Erro ao remover: {str(e)}. Tente novamente mais tarde.", nivel="ERROR", tipo_flash="danger", contexto_extra={'id': id})
    return redirect(url_for('equipamento_route.listar_Equipamento'))

# =================== Ocupado Equipamento ===================
@equipamento_route.route("/ocupado", methods=['GET', 'POST'])
@admin_suporte_auth
def ocupado_Equipamento():    
    return render_template('Equipamentos/ocupado.html')
