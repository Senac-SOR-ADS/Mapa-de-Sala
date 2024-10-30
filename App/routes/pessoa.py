from flask import render_template, Blueprint, request, flash, redirect, url_for
from App.routes.auth.autenticar import login_auth
from App.controller.pessoa import cadastrarPessoa, buscaPessoas

# Definindo o blueprint
pessoa_route = Blueprint('pessoa_route', __name__, template_folder='templates/Funcionarios/')

@pessoa_route.route("/", methods=['GET', 'POST'])
@login_auth
def listarFuncionario():
    try:
        valores = buscaPessoas()
    except Exception as e:
        flash(f'Erro ao listar funcionários: {str(e)}', 'danger')
        valores = []

    return render_template('Funcionarios/listar.html', valores=valores)

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
        
                # Verificação de e-mail existente
        # if email_existe(email):  # Função que verifica se o e-mail já existe no banco
        #     flash('Este e-mail já está registrado. Por favor, use um e-mail diferente.', 'danger')
        #     return render_template('Funcionarios/cadastrar.html')

        # Modificando a data
        dataNasc_modificada = modificarData(dataNasc)
        if dataNasc_modificada is None:
            flash('Data de nascimento inválida. Por favor, insira no formato AAAA-MM-DD.', 'danger')
            return render_template('Funcionarios/cadastrar.html')

        try:
            cadastrarPessoa(nome, cpfCnpj, dataNasc_modificada, telefone, email, cargo)
            flash('Funcionário cadastrado com sucesso!', 'success')
            return redirect(url_for('pessoa_route.cadastrarFuncionario'))
        except Exception as e:
            flash(f'Erro ao cadastrar funcionário: {str(e)}', 'danger')

    return render_template('Funcionarios/cadastrar.html')

# Verifica se a data está no formato 'AAAA-MM-DD e Retorna a data no formato 'DD/MM/AAAA''
def modificarData(dataNasc):
    if '-' in dataNasc:
        data = dataNasc.split('-')
        if len(data) == 3:
            return f'{data[2]}/{data[1]}/{data[0]}'    
    return None

@pessoa_route.route('/editar/<int:id>', methods=['GET'])
@login_auth
def EditarFuncionario():
    return render_template('/Funcionarios/editar.html')
