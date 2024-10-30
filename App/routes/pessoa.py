from flask import render_template, Blueprint, request, flash, redirect, url_for
from App.routes.auth.autenticar import login_auth
from App.controller.pessoa import cadastrarPessoa, buscaPessoas

# Definindo o blueprint
pessoa_route = Blueprint('pessoa_route', __name__, template_folder='templates/Funcionarios/')

@pessoa_route.route("/", methods=['GET', 'POST'])
@login_auth
def listarFuncionario():
    page = request.args.get('page', 1, type=int)
    per_page = 10

    try:
        all_employees = buscaPessoas()
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

@pessoa_route.route("/cadastrar", methods=['GET', 'POST'])
@login_auth
def cadastrarFuncionario():
    if request.method == 'POST':
        if request.is_json:
            dados = request.get_json()
            print('Dados recebidos (JSON):', dados)  
        else:
            dados = request.form
            print('Dados recebidos (Formulário):', dados)

        # Captura os campos do formulário
        nome = dados.get('nome')
        cpfCnpj = dados.get('cpfCnpj')
        dataNasc = dados.get('dataNasc')
        telefone = dados.get('telefone')
        email = dados.get('email')
        cargo = dados.get('cargo')

        # Validação dos campos obrigatórios
        if not all([nome, cpfCnpj, dataNasc, telefone, email, cargo]):
            flash('Todos os campos são obrigatórios.', 'danger')
            return render_template('Funcionarios/cadastrar.html')

        try:
            cadastrarPessoa(nome, cpfCnpj, dataNasc, telefone, email, cargo)
            flash('Funcionário cadastrado com sucesso!', 'success')
            return redirect(url_for('pessoa_route.cadastrarFuncionario'))
        except Exception as e:
            flash(f'Erro ao cadastrar funcionário: {str(e)}', 'danger')

    return render_template('Funcionarios/cadastrar.html')


@pessoa_route.route('/editar/<int:id>', methods=['GET'])
@login_auth
def EditarFuncionario():
    return render_template('/Funcionarios/editar.html')
