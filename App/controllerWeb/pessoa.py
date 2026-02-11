from App.model.pessoa import Pessoa
from App.controllerWeb.login import cadastrarLogin, atualizarCadastro
from App.controllerWeb.utils import formatarCpf, formatarCnpj, formatarTelefone
from App.model.logger import logger

# =================== cadastrar ===================
def cadastrarPessoa(nome: str, cpf_cnpj: str, data_nasc: str, telefone: str, email: str, cargo: str) -> dict:
    """ Cadastra uma nova pessoa e seu login associado no banco de dados. """
    try:
        id_pessoa = Pessoa().cadastrar(nome, cpf_cnpj, data_nasc, telefone, email, cargo)
        
        if id_pessoa:
            return cadastrarLogin(id_pessoa, cpf_cnpj, email, cargo)
        
        return {"error": "Não foi possível cadastrar a pessoa."}
    
    except Exception as e:
        logger.error("Erro ao cadastrar pessoa: %s", str(e))
        return {"error": "Erro ao cadastrar pessoa."}

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
        logger.error("Erro ao atualizar os dados: %s", str(e))
        return {"error": "Erro ao atualizar os dados."}

# =================== listar ===================
def buscarPessoas(search_query: str = '') -> dict:
    """ Retorna um dicionário com as pessoas cadastradas, usando o nome como chave e o ID como valor. Search_query filtra pelo nome se fornecido. """
    try:
        todasPessoas = Pessoa.buscar()

        if search_query:
            todasPessoas = [p for p in todasPessoas if search_query.lower() in p[1].lower()]

        return {i[1]: i[0] for i in todasPessoas} if todasPessoas else {}
    except Exception as e:
        logger.error("Erro ao listar pessoas: %s", str(e))
        return {"error": "Erro ao listar pessoas."}

# =================== Remover ===================
def removerPessoa(idPessoa: int) -> dict:
    """ Remove uma pessoa do banco de dados pelo ID. """
    try:
        if Pessoa.deletar(idPessoa):
            return {"success": "Pessoa removida com sucesso."}
        return {"error": "Não foi possível remover a pessoa."}
    except Exception as e:
        logger.error("Erro ao remover pessoa: %s", str(e))
        return {"error": "Erro ao remover pessoa."}

# =================== buscar Id ===================
def buscarPessoaId(idPessoa: int) -> dict:
    """ Busca uma pessoa pelo ID e retorna suas informações ou uma mensagem de erro se não for encontrada. """
    if not isinstance(idPessoa, int):
        return {"error": "ID inválido. Deve ser um número inteiro."}

    try:
        resultado = Pessoa.pesquisar_id(idPessoa)

        if not resultado or len(resultado) < 7:
            return {"error": "Pessoa não encontrada"}
        
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
        logger.error("Erro ao buscar pessoa: %s", str(e))
        return {"error": "Erro ao buscar pessoa."}
