from flask import flash, render_template, Blueprint, request, redirect, url_for
from App.routes.auth.autenticar import admin_auth, admin_suporte_auth, login_auth
from App.controllerWeb.pessoa import cadastrarPessoa, buscarPessoas, buscarPessoaId, atualizarPessoa, removerPessoa
from App.routes.utils import processar_mensagem, processar_resultado, processar_paginacao, processar_validacao, renderizar_com_mensagem
from App.controllerWeb.login import pegarUsuarioLogado
from App.controllerWeb.login import atualizarCadastro

funcionario_route = Blueprint('funcionario_route', __name__, template_folder='templates/Funcionarios/')

# -------------------------- Funções Auxiliares ------------------------
CAMPOS_FUNCIONARIO = ['nome', 'cpfCnpj', 'dataNasc', 'telefone', 'email', 'cargo']
VALIDACOES = {
    'nome': lambda nome: True if 3 <= len(nome) <= 100 and nome.replace(' ', '').isalnum() else "O nome deve ter entre 3 e 100 caracteres e ser alfanumérico.",
    'cpfCnpj': lambda cpfCnpj: True if cpfCnpj.isdigit() and len(cpfCnpj) in [11, 14] else "CPF/CNPJ inválido."
}

def processar_dados(dados: dict) -> dict: 
    return {campo: dados.get(campo, '').strip() for campo in CAMPOS_FUNCIONARIO}

def validar(dados: dict) -> bool: 
    return processar_validacao(dados, tipo="obrigatorio", validacoes_adicionais=VALIDACOES)

# =================== Listar Funcionários ===================
@funcionario_route.route("/", methods=['GET'])
@admin_suporte_auth
def listar_Pessoa():
    page, per_page, search_query = request.args.get('page', 1, type=int), 10, request.args.get('search', '', type=str)
    try:
        funcionarios_dict = buscarPessoas(search_query)
        if not isinstance(funcionarios_dict, dict):
            raise ValueError("Erro ao listar funcionários. Verifique a conexão ou os parâmetros de pesquisa.")
        employee_list = list(funcionarios_dict.items())
        funcionarios_paginated, total_items, total_pages, current_page, has_next, has_prev = processar_paginacao(employee_list, page, per_page)
        return render_template('Funcionarios/listar.html', valores=funcionarios_paginated, total_items=total_items, total_pages=total_pages, page=current_page, per_page=per_page, search_query=search_query, has_next=has_next, has_prev=has_prev)
    except Exception as e:
        processar_mensagem(mensagem=str(e), nivel="ERROR", tipo_flash="danger")
        return redirect(url_for('funcionario_route.listar_Pessoa'))

# =================== Cadastrar Funcionário ===================
@funcionario_route.route("/cadastrar", methods=['GET', 'POST'])
@admin_suporte_auth
def cadastrar_Pessoa():
    if request.method == 'POST':
        dados = request.form.to_dict()
        if not validar(dados): 
            return render_template('Funcionarios/cadastrar.html', mensagem="Campos obrigatórios incorretos. Verifique os dados inseridos.")
        dados_processados = processar_dados(dados)
        try:
            result = cadastrarPessoa(*dados_processados.values())
            mensagem_sucesso = f"Funcionário {dados['nome']} cadastrado com sucesso!"
            if processar_resultado(result, mensagem_sucesso, "Erro ao cadastrar funcionário. Verifique os dados e tente novamente."):
                return redirect(url_for('funcionario_route.listar_Pessoa'))
        except Exception as e:
            processar_mensagem(mensagem=f"Erro ao cadastrar: {str(e)}. Tente novamente mais tarde.", nivel="ERROR", tipo_flash="danger")
    return render_template('Funcionarios/cadastrar.html')

# =================== Atualizar Funcionário ===================
@funcionario_route.route('/editar/<int:id>', methods=['GET', 'POST'])
@admin_suporte_auth
def editar_Pessoa(id):
    try:
        funcionario = buscarPessoaId(id)
        if not funcionario or 'error' in funcionario:
            raise ValueError(f"Funcionário com ID {id} não encontrado. Verifique o ID e tente novamente.")
        if request.method == 'POST':
            dados = request.form.to_dict()
            if not validar(dados):
                return render_template('Funcionarios/editar.html', funcionario=funcionario, mensagem="Dados inválidos. Verifique os campos.")
            dados_processados = processar_dados(dados)
            result = atualizarPessoa(id, **dados_processados)
            if "login_update" in result: 
                processar_mensagem(mensagem=f"Funcionário {dados['nome']} atualizado com sucesso! Cargo: {dados['cargo']}", nivel="INFO", tipo_flash="success")
                return redirect(url_for('funcionario_route.listar_Pessoa'))
            else:
                processar_mensagem(mensagem="Erro ao atualizar o funcionário. Verifique os dados e tente novamente.", nivel="ERROR", tipo_flash="danger")
    except Exception as e:
        processar_mensagem(mensagem=str(e), nivel="ERROR", tipo_flash="danger")
    return render_template('Funcionarios/editar.html', funcionario=funcionario)

# =================== Remover Funcionário ===================
@funcionario_route.route('/remover/<int:id>', methods=['GET'])
@admin_auth
def remover_Pessoa(id):
    try:
        result = removerPessoa(id)
        if not processar_resultado(result, f"Funcionário com ID {id} removido com sucesso!", f"Erro ao remover o funcionário com ID {id}. Verifique o ID e tente novamente."):
            raise Exception(f"Falha ao remover o funcionário com ID {id}.")
    except Exception as e:
        processar_mensagem(mensagem=f"Erro ao remover: {str(e)}. Tente novamente mais tarde.", nivel="ERROR", tipo_flash="danger", contexto_extra={'id': id})
    return redirect(url_for('funcionario_route.listar_Pessoa'))

# =================== Perfil ===================
@funcionario_route.route('/perfil', methods=['GET', 'POST'])
@login_auth
def perfil():
    usuario_logado = pegarUsuarioLogado()  # Chama a função no controller
    if usuario_logado is None:
        flash("Você precisa estar logado para acessar esta página.", "danger")
        return redirect(url_for('login_route.login'))

    id_pessoa = usuario_logado.get('id_pessoa')

    try:
        if not id_pessoa:
            raise ValueError("ID de pessoa não encontrado na sessão.")

        funcionario = buscarPessoaId(id_pessoa)
        if not funcionario or 'error' in funcionario:
            raise ValueError(f"Funcionário com ID {id_pessoa} não encontrado.")

        # Adicionando o nível de acesso ao perfil
        nivel_acesso = usuario_logado.get('nivel_acesso')  # Obtém o nível de acesso

        if request.method == 'POST':
            novaSenha = request.form.get('senha')
            email_atual = funcionario.get('email')
            cargo_atual = funcionario.get('cargo')

            if not novaSenha:
                flash("A senha não foi fornecida.", "warning")
                return redirect(url_for('funcionario_route.perfil'))

            dados_atualizados = {
                "idLogin": usuario_logado['id_login'],
                "novaSenha": novaSenha,
                "novoEmail": email_atual,
                "novoCargo": cargo_atual
            }

            resultado = atualizarCadastro(**dados_atualizados)

            if processar_resultado(resultado, "Senha atualizada com sucesso!", "Erro ao atualizar a senha."):
                return redirect(url_for('funcionario_route.perfil'))

    except Exception as e:
        processar_mensagem(mensagem=str(e), nivel="ERROR", tipo_flash="danger")

    return render_template('Funcionarios/perfil.html', funcionario=funcionario, nivel_acesso=nivel_acesso)




