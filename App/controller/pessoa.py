from App.model.pessoa import Pessoa
from App.controller.login import cadastrarLogin, atualizarCadastro

# =================== cadastrar ===================
def cadastrarPessoa(nome, cpf_cnpj, data_nasc, telefone, email, cargo):
    """Cadastra uma nova pessoa e seu login associado no banco de dados."""
    
    try:
        id_pessoa = Pessoa().cadastrar(nome, cpf_cnpj, data_nasc, telefone, email, cargo)
        if id_pessoa:
            return cadastrarLogin(id_pessoa, cpf_cnpj, email, cargo)
        return {"error": "Não foi possível cadastrar a pessoa."}
    
    except Exception as e:
        return {"error": f"Erro ao cadastrar pessoa: {e}"}

# =================== atualizar ===================
def atualizarPessoa(idPessoa, nome, cpfCnpj, dataNasc, telefone, email, cargo): 
    """Atualiza os dados de uma pessoa existente no banco de dados e seu cadastro de login."""

    try:
        pessoaModel = Pessoa()
        if pessoaModel.atualizar(idPessoa, nome, cpfCnpj, dataNasc, telefone, email, cargo):
            return {
                "success": "Dados da pessoa atualizados com sucesso.",
                "login_update": atualizarCadastro(idPessoa, email, cargo)
            }
        return {"error": "Falha ao atualizar os dados da pessoa."}
    
    except Exception as e:
        return {"error": f"Erro ao atualizar os dados: {e}"}

# =================== listar ===================
def buscarPessoas() -> dict:
    """Retorna um dicionário com todas as pessoas cadastradas, usando o nome como chave e o ID como valor."""

    todasPessoas = Pessoa.buscar()
    return {i[1]: i[0] for i in todasPessoas} if todasPessoas else {}

# =================== buscar Id ===================
def buscarPessoaId(idPessoa):
    """Busca uma pessoa pelo ID e retorna suas informações ou uma mensagem de erro se não for encontrada."""
    
    if not isinstance(idPessoa, int):
        return {"error": "ID inválido. Deve ser um número inteiro."}

    try:
        resultado = Pessoa.pesquisar_id(idPessoa)

        if not resultado or len(resultado) < 7:
            return {"error": "Pessoa não encontrada"}

        return {
            "idPessoa": resultado[0],
            "nome": resultado[1],
            "cpfCnpj": resultado[2],
            "dataNasc": resultado[3],
            "telefone": resultado[4],
            "email": resultado[5],
            "cargo": resultado[6],
        }
    except Exception as e:
        return {"error": f"Erro ao buscar pessoa: {str(e)}"}

# =================== Remove ===================
def removerPessoa(idPessoa):
    """Remove uma pessoa do banco de dados pelo ID."""
    return Pessoa.deletar(idPessoa)