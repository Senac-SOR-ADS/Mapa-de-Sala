from flask import render_template, Blueprint, request, jsonify
from App.routes.login import login_required
from App.controller.area import cadastroDeArea, listarAreas

# Definindo o blueprint
area_route = Blueprint('area_route', __name__, template_folder='templates')


@area_route.route("/", methods=['GET', 'POST'])
@login_required
def area():
    return render_template('area.html', valores=listarAreas())


@area_route.route("/cadastrar", methods=['GET', 'POST'])
@login_required
def cadastrarArea():
    if request.method == 'POST':
        try:
            if request.is_json:
                dados = request.get_json()
                print('Dados recebidos (JSON):', dados)
            else:
                dados = request.form
                print('Dados recebidos (Formulário):', dados)

            # Captura os campos do formulário
            nomeArea = dados.get('nomeArea')

            # Cadastrando a área
            resultado = cadastroDeArea(nomeArea)

            return jsonify({'mensagem': ' Area cadastrada com sucesso!', 'resultado': resultado}), 201

        except Exception as e:
            return jsonify({'erro': f'Erro inesperado: {str(e)}'}), 500

    return render_template('cadastrarArea.html')

