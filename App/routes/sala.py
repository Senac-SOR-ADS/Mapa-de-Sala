from flask import render_template, Blueprint, request, jsonify
from App.routes.login import login_required
from App.controller.sala import cadastrarSala, listarSala

# Definindo o blueprint
sala_route = Blueprint('sala_route', __name__, template_folder='templates')

@sala_route.route("/", methods=['GET', 'POST'])
@login_required
def sala():
    return render_template('sala.html', valores=listarSala())

@sala_route.route("/cadastrar", methods=['GET', 'POST'])
@login_required
def cadastrar_Sala():
    if request.method == 'POST':
        try:
            if request.is_json:
                dados = request.get_json()
                print('Dados recebidos (JSON):', dados)  
            else:
                dados = request.form
                print('Dados recebidos (Formulário):', dados)

            # Captura os campos do formulário
            nome = dados.get('nome')
            tipo = dados.get('tipo')
            predio = dados.get('predio')  
            equipamento = dados.get('equipamento')
            capacidade = dados.get('capacidade')
            feedback = dados.get('feedback')

            # Validação dos campos
            if not all([nome, tipo, predio, equipamento, capacidade, feedback]):
                return jsonify({'erro': 'Todos os campos são obrigatórios.'}), 400

            # Cadastrando o curso
            resultado = cadastrarSala(nome, tipo, predio, equipamento, capacidade, feedback)
            return jsonify({'mensagem': 'Sala cadastrada com sucesso!', 'resultado': resultado}), 201

        except Exception as e:
            return jsonify({'erro': f'Erro inesperado: {str(e)}'}), 500
           
    return render_template('cadastrarSala.html')