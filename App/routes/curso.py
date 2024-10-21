from flask import render_template, Blueprint, request, jsonify
from App.routes.login import login_required
from App.controller.curso import cadastrarCurso, listarCursos
from App.controller.area import listarAreas

# Definindo o blueprint
curso_route = Blueprint('curso_route', __name__, template_folder='templates')

@curso_route.route("/", methods=['GET', 'POST'])
@login_required
def curso():
    return render_template('curso.html', valores=listarCursos())

@curso_route.route("/cadastrar", methods=['GET', 'POST'])
@login_required
def cadastrar_Curso():
    if request.method == 'POST':
        try:
            if request.is_json:
                dados = request.get_json()
                print('Dados recebidos (JSON):', dados)  
            else:
                dados = request.form
                print('Dados recebidos (Formulário):', dados)

            # Captura os campos do formulário
            area = dados.get('area')
            nome = dados.get('nome')
            oferta = dados.get('oferta')
            periodo = dados.get('periodo')
            carga = dados.get('carga')
            horas = dados.get('horas')
            alunos = dados.get('alunos')

            # Validação dos campos
            if not all([area, nome, oferta, periodo, carga, horas, alunos]):
                return jsonify({'erro': 'Todos os campos são obrigatórios.'}), 400

            # Cadastrando o curso
            resultado = cadastrarCurso(area, nome, oferta, periodo, carga, horas, alunos)

            return jsonify({'mensagem': 'Curso cadastrado com sucesso!', 'resultado': resultado}), 201

        except Exception as e:
            return jsonify({'erro': f'Erro inesperado: {str(e)}'}), 500
    
    elif request.method == 'GET':
        return render_template('cadastrarCurso.html', valores=listarAreas())


    
