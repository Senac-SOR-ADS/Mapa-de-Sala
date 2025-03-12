from App.model.pessoa import Pessoa
from App.controller.login import cadastrarLogin, atualizarCadastro
from App.controller.utils import formatarCpf, formatarCnpj, formatarTelefone, validarInputs

# =================== cadastrar ===================
def cadastrarPessoa(nome: str, cpf_cnpj: str, data_nasc: str, telefone: str, email: str, cargo: str) -> dict:
    """ Cadastra uma nova pessoa e seu login associado no banco de dados. """

    # Validar todos os campos de entrada
    if not validarInputs([nome, cpf_cnpj, data_nasc, telefone, email, cargo]):
        return {"error": "Preencha todos os campos corretamente."}

    try:
        # Cadastro da pessoa no banco de dados
        id_pessoa = Pessoa().cadastrar(nome, cpf_cnpj, data_nasc, telefone, email, cargo)
        
        if id_pessoa:
            # Cadastro do login associado à pessoa
            return cadastrarLogin(id_pessoa, cpf_cnpj, email, cargo)
        
        return {"error": "Não foi possível cadastrar a pessoa."}
    
    except Exception as e:
        return {"error": f"Erro ao cadastrar pessoa: {str(e)}"}

# =================== atualizar ===================
def atualizarPessoa(idPessoa: int, nome: str, cpfCnpj: str, dataNasc: str, telefone: str, email: str, cargo: str) -> dict:
    """ Atualiza os dados de uma pessoa existente no banco de dados e seu cadastro de login. """
    try:
        pessoaModel = Pessoa()
        if pessoaModel.atualizar(idPessoa, nome, cpfCnpj, dataNasc, telefone, email, cargo):
            return {
                "login_update": atualizarCadastro(idPessoa, email, cargo)
            }
        return {"error": "Falha ao atualizar os dados da pessoa."}
    
    except Exception as e:
        return {"error": f"Erro ao atualizar os dados: {str(e)}"}

# =================== listar ===================
def buscarPessoas(search_query: str = '') -> dict:
    """ Retorna um dicionário com as pessoas cadastradas, usando o nome como chave e o ID como valor. Search_query filtra pelo nome se fornecido. """
    print('buscou pessoa')
    try:
        todasPessoas = Pessoa.buscar()

        if search_query:
            todasPessoas = [p for p in todasPessoas if search_query.lower() in p[1].lower()]
        return {i[0]: i[1] for i in todasPessoas} if todasPessoas else {}
    except Exception as e:
        return {"error": f"Erro ao listar pessoas: {str(e)}"}

# =================== Remover ===================
def removerPessoa(idPessoa: int) -> dict:
    """ Remove uma pessoa do banco de dados pelo ID. """
    try:
        if Pessoa.deletar(idPessoa):
            return {"success": "Pessoa removida com sucesso."}
        return {"error": "Não foi possível remover a pessoa."}
    except Exception as e:
        return {"error": f"Erro ao remover pessoa: {str(e)}"}

# =================== buscar Id ===================
def buscarPessoaId(idPessoa: int) -> dict:
    """ Busca uma pessoa pelo ID e retorna suas informações ou uma mensagem de erro se não for encontrada. """
    if not isinstance(idPessoa, int):
        return {"error": "ID inválido. Deve ser um número inteiro."}

    try:
        resultado = Pessoa.pesquisar_id(idPessoa)

        if not resultado or len(resultado) < 7:
            return {"error": "Pessoa não encontrada"}

        # Formatando CPF, CNPJ e Telefone
        cpfCnpj_formatado = formatarCpf(resultado[2]) if len(resultado[2]) == 11 else formatarCnpj(resultado[2])
        telefone_formatado = formatarTelefone(resultado[4])

        return {
            "idPessoa": resultado[0],
            "nome": resultado[1],
            "cpfCnpj": cpfCnpj_formatado,
            "dataNasc": resultado[3],
            "telefone": telefone_formatado,
            "email": resultado[5],
            "cargo": resultado[6],
        }
    except Exception as e:
        return {"error": f"Erro ao buscar pessoa: {str(e)}"}