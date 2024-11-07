from flask import render_template, Blueprint, request, flash, redirect, url_for
from App.routes.auth.autenticar import login_auth
from App.controller.pessoa import cadastrarPessoa, buscarPessoas, buscarPessoaId, atualizarPessoa, removerPessoa

funcionario_route = Blueprint('funcionario_route', __name__, template_folder='templates/Funcionarios/')

# =================== listar ===================
@funcionario_route.route("/", methods=['GET'])
@login_auth
def listar_Pessoa():
    page = request.args.get('page', 1, type=int)
    per_page = 10

    try:
        all_employees = buscarPessoas()
        if not isinstance(all_employees, dict):
            raise ValueError("Esperava um dicionário de funcionários")

        employee_list = [(key, value) for key, value in all_employees.items()]
        total_items = len(employee_list)
        start = (page - 1) * per_page
        end = start + per_page
        funcionarios_paginated = employee_list[start:end]

    except Exception as e:
        flash(f'Erro ao listar funcionários: {str(e)}', 'danger')
        return render_template('Funcionarios/listar.html', valores=[], total_items=0, page=1, per_page=per_page)
    return render_template('Funcionarios/listar.html', valores=funcionarios_paginated, total_items=total_items, page=page, per_page=per_page)

# =================== cadastrar ===================
@funcionario_route.route("/cadastrar", methods=['GET', 'POST'])
@login_auth
def cadastrar_Pessoa():
    if request.method == 'POST':
        dados = request.form
        nome = dados.get('nome')
        cpfCnpj = dados.get('cpfCnpj')
        dataNasc = dados.get('dataNasc')
        telefone = dados.get('telefone')
        email = dados.get('email')
        cargo = dados.get('cargo')
    
        if not all([nome, cpfCnpj, dataNasc, telefone, email, cargo]):
            flash('Todos os campos são obrigatórios.', 'danger')
            return render_template('Funcionarios/cadastrar.html')

        try:
            if cadastrarPessoa(nome, cpfCnpj, dataNasc, telefone, email, cargo):
                flash('Funcionário cadastrado com sucesso!', 'success')
                return redirect(url_for('funcionario_route.listar_Pessoa'))
            else:
                flash('Erro ao cadastrar funcionário.', 'danger')
        except Exception as e:
            flash(f'Erro ao cadastrar funcionário: {str(e)}', 'danger')
    return render_template('Funcionarios/cadastrar.html')

# =================== atualizar ===================
@funcionario_route.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_auth
def editar_Pessoa(id):
    funcionario = buscarPessoaId(id)
    
    if request.method == 'GET':
        if 'error' in funcionario:
            flash(funcionario['error'], 'danger')
            return redirect(url_for('funcionario_route.listar_Pessoa'))
        return render_template('Funcionarios/editar.html', funcionario=funcionario)

    if request.method == 'POST':
        dados = request.form
        nome = dados.get('nome')
        cpfCnpj = dados.get('cpfCnpj')
        dataNasc = dados.get('dataNasc')
        telefone = dados.get('telefone')
        email = dados.get('email')
        cargo = dados.get('cargo')

        if not all([nome, cpfCnpj, dataNasc, telefone, email, cargo]):
            flash('Todos os campos são obrigatórios.', 'danger')
            return render_template('Funcionarios/editar.html', funcionario=funcionario)

        try:
            if atualizarPessoa(id, nome, cpfCnpj, dataNasc, telefone, email, cargo):
                flash('Funcionário atualizado com sucesso!', 'success')
                return redirect(url_for('funcionario_route.listar_Pessoa'))
            else:
                flash('Erro ao atualizar funcionário.', 'danger')
        except Exception as e:
            flash(f'Erro ao atualizar funcionário: {str(e)}', 'danger')
    return render_template('Funcionarios/editar.html', funcionario=funcionario)

# =================== Remove ===================
@funcionario_route.route('/remover/<int:id>', methods=['GET'])
@login_auth
def remover_Pessoa(id):
    """Remove uma pessoa do banco de dados pelo ID."""
    try:
        if removerPessoa(id):
            flash('Funcionário removido com sucesso!', 'success')
        else:
            flash('Erro ao remover funcionário.', 'danger')
    except Exception as e:
        flash(f'Erro ao remover funcionário: {str(e)}', 'danger')
    
    return redirect(url_for('funcionario_route.listar_Pessoa'))
