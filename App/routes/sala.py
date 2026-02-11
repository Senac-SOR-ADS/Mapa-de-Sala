from flask import render_template, Blueprint, request, redirect, url_for
from App.routes.auth.autenticar import admin_auth, admin_suporte_auth
from App.controllerWeb.sala import listarSala, cadastrarSala, buscarSalaId, atualizarSala, removerSala
from App.routes.utils import processar_mensagem, processar_resultado, processar_paginacao, processar_validacao

sala_route = Blueprint('sala_route', __name__, template_folder='templates/Salas/')

# Funções Auxiliares
CAMPOS_SALA = ['nome', 'tipo', 'predio', 'equipamento', 'capacidade', 'feedback']

def processar_dados(dados: dict) -> dict: 
    return {campo: dados.get(campo, '').strip() for campo in CAMPOS_SALA}

VALIDACOES_SALA = {
    'nome': lambda nome: True if 3 <= len(nome) <= 100 and nome.replace(' ', '').isalnum() else "O nome deve ter entre 3 e 100 caracteres e ser alfanumérico.",
    'tipo': lambda tipo: True if 3 <= len(tipo) <= 100 else "O tipo deve ter entre 3 e 100 caracteres.",
    'predio': lambda predio: True if 3 <= len(predio) <= 100 else "O prédio deve ter entre 3 e 100 caracteres.",
    'capacidade': lambda capacidade: True if capacidade.isdigit() and 1 <= int(capacidade) <= 500 else "A capacidade deve ser um número entre 1 e 500.",
    'equipamento': lambda equipamento: True if equipamento == '' or len(equipamento) <= 100 else "O campo equipamento pode ter até 100 caracteres.",
    'feedback': lambda feedback: True if feedback == '' or len(feedback) <= 500 else "O campo feedback pode ter até 500 caracteres."
}

OBRIGATORIOS = ['nome', 'tipo', 'predio', 'capacidade']

def validar(dados: dict) -> bool:
    campos_obrigatorios = {campo: dados.get(campo) for campo in OBRIGATORIOS}
    if not processar_validacao(campos_obrigatorios, tipo="obrigatorio"):
        return {'error': 'Preencha todos os campos corretamente.', 'detalhes': 'Campos obrigatórios não preenchidos.'}

    validacoes_adicionais = {campo: VALIDACOES_SALA[campo] for campo in dados if campo in VALIDACOES_SALA and campo not in OBRIGATORIOS}
    
    for campo, validacao in validacoes_adicionais.items():
        valor = dados.get(campo, '')
        resultado_validacao = validacao(valor)
        if resultado_validacao != True:
            return {'error': 'Erro de validação.', 'detalhes': f'Erro no campo {campo}: {resultado_validacao}'}
    
    return True

# =================== Listagem de Salas ===================
@sala_route.route("/", methods=['GET'])
@admin_suporte_auth
def listar_Sala():
    page, per_page, search_query = request.args.get('page', 1, type=int), 10, request.args.get('search', '', type=str)
    try:
        all_rooms = listarSala(search_query)
        if not isinstance(all_rooms, dict): raise ValueError("Esperava um dicionário de salas")
        room_list = list(all_rooms.items())
        salas_paginated, total_items, total_pages, current_page, has_next, has_prev = processar_paginacao(room_list, page, per_page)
    except Exception as e:
        processar_mensagem(mensagem=f'Erro ao listar salas: {str(e)}', nivel="ERROR", tipo_flash="danger")
        return render_template('Salas/listar.html', valores=[], total_items=0, page=1, per_page=per_page, search_query=search_query)
    
    return render_template('Salas/listar.html', valores=salas_paginated, total_items=total_items, total_pages=total_pages, page=current_page, per_page=per_page, search_query=search_query, has_next=has_next, has_prev=has_prev)

# =================== Cadastro de Sala ===================
@sala_route.route("/cadastrar", methods=['GET', 'POST'])
@admin_suporte_auth
def cadastrar_Sala():
    if request.method == 'POST':
        dados = request.form
        
        validacao = validar(dados)
        
        if validacao is not True:
            return render_template('Salas/cadastrar.html', mensagem="Campos obrigatórios incorretos.", detalhes=validacao['detalhes'])
        
        dados_processados = processar_dados(dados)
        
        try:
            result = cadastrarSala(*dados_processados.values())
            
            if not result:
                processar_mensagem(mensagem="Falha ao cadastrar a sala. Erro no banco de dados ou nos dados.", nivel="ERROR", tipo_flash="danger")
                return render_template('Salas/cadastrar.html', mensagem="Falha ao cadastrar a sala.")
            
            mensagem_sucesso = f"Sala {dados['nome']} cadastrada com sucesso!"
            
            if processar_resultado(result, mensagem_sucesso, "Falha ao cadastrar a sala."): 
                return redirect(url_for('sala_route.listar_Sala'))
        
        except Exception as e:
            processar_mensagem(mensagem=f'Erro ao cadastrar sala: {str(e)}', nivel="ERROR", tipo_flash="danger")
            return render_template('Salas/cadastrar.html', mensagem="Falha ao cadastrar a sala.")
    
    return render_template('Salas/cadastrar.html')

# =================== Edição de Sala ===================
@sala_route.route('/editar/<int:id>', methods=['GET', 'POST'])
@admin_suporte_auth
def editar_Sala(id):
    sala = buscarSalaId(id)
    if sala.get('error'):
        processar_mensagem(mensagem=f"Erro ao buscar a sala com ID {id}: {sala['error']}", nivel="ERROR", tipo_flash="danger")
        return redirect(url_for('sala_route.listar_Sala'))
    if request.method == 'POST':
        dados = request.form
        validacao = validar(dados)
        if validacao is not True: 
            return render_template('Salas/editar.html', sala=sala, mensagem="Campos incorretos.", detalhes=validacao['detalhes'])
        
        dados_processados = processar_dados(dados)
        mensagem_sucesso = f"Sala {dados['nome']} com ID {id} atualizada com sucesso!"
        result = atualizarSala(*dados_processados.values(), id)
        if processar_resultado(result, mensagem_sucesso, "Falha ao atualizar a sala."): 
            return redirect(url_for('sala_route.listar_Sala'))
    return render_template('Salas/editar.html', sala=sala)

# =================== Remoção de Sala ===================
@sala_route.route('/remover/<int:id>', methods=['GET'])
@admin_auth
def remover_Sala(id):
    try:
        result = removerSala(id)
        processar_resultado(result, "Sala removida com sucesso!", "Falha ao remover a sala. Verifique o ID e tente novamente.")
    except Exception as e:
        processar_mensagem(mensagem=f'Erro ao remover sala: {str(e)}', nivel="ERROR", tipo_flash="danger")
    return redirect(url_for('sala_route.listar_Sala'))
