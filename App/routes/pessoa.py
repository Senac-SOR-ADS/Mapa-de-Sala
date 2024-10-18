from flask import render_template, Blueprint, request, jsonify
from App.routes.login import login_required
from App.controller.pessoa import cadastrarPessoa

# Definindo o blueprint
pessoa_route = Blueprint('pessoa_route', __name__, template_folder='templates')

@pessoa_route.route("/", methods=['GET', 'POST'])
@login_required
def funcionario():
    return render_template('funcionario.html')

@pessoa_route.route("/cadastrar", methods=['GET', 'POST'])
@login_required
def cadastrar_Funcionario():
    if request.method == 'POST':
        try:
            # Verifica se a requisição é JSON ou Formulário
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

            # Modificando a data
            dataNasc_modificada = modificarData(dataNasc)
            if dataNasc_modificada is None:
                return jsonify({'erro': 'Data de nascimento inválida. Formato esperado: YYYY-MM-DD'}), 400

            # Cadastrando a pessoa
            resultado = cadastrarPessoa(nome, cpfCnpj, dataNasc_modificada, telefone, email, cargo)

            return jsonify({'mensagem': 'Pessoa cadastrada com sucesso!', 'resultado': resultado}), 201

        except Exception as e:
            return jsonify({'erro': f'Erro inesperado: {str(e)}'}), 500

    # Se o método for GET, renderiza o template do formulário
    return render_template('cadastrarFuncionario.html')

def modificarData(dataNasc):
    if '-' in dataNasc:
        data = dataNasc.split('-')
        if len(data) == 3:
            return f'{data[2]}/{data[1]}/{data[0]}'    
    return None
