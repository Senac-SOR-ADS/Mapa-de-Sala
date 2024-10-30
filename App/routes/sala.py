from flask import render_template, Blueprint, request, flash, redirect, url_for
from App.routes.auth.autenticar import login_auth
from App.controller import sala

# Definindo o blueprint
sala_route = Blueprint('sala_route', __name__, template_folder='templates/Salas/')

@sala_route.route("/", methods=['GET', 'POST'])
@login_auth
def listarSalas():
    try:
        valores = sala.listarSala()
    except Exception as e:
        flash(f'Erro ao listar salas: {str(e)}', 'danger')
        valores = []
    return render_template('/Salas/listar.html', valores=valores)

@sala_route.route("/cadastrar", methods=['GET', 'POST'])
@login_auth
def cadastrarSala():
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
            if not all([nome, tipo, predio, capacidade]):
                flash('Todos os campos (nome, tipo, prédio e capacidade) são obrigatórios.', 'danger')
                return render_template('/Salas/cadastrar.html')

            # Cadastrando a sala
            resultado = sala.cadastrarSala(nome, tipo, predio, equipamento, capacidade, feedback)
            flash('Sala cadastrada com sucesso!', 'success')
            return redirect(url_for('sala_route.cadastrarSala'))
        except Exception as e:
            flash(f'Erro ao cadastrar a sala: {str(e)}', 'danger')
 
    return render_template('/Salas/cadastrar.html')

@sala_route.route('/editar/<int:id>', methods=['GET'])
@login_auth
def editarSala():
    return render_template('/Salas/editar.html')
