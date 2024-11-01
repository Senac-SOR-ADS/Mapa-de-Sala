from App.model.pessoa import Pessoa

def cadastrarPessoa(nome, cpfCnpj, dataNasc, telefone, email, cargo):
    """Cadastra uma nova pessoa no banco de dados."""
    pessoaModel = Pessoa()
    return pessoaModel.cadastrar(nome, cpfCnpj, dataNasc, telefone, email, cargo)

def buscarPessoas() -> dict:
    """Busca todas as pessoas cadastradas e retorna um dicionário com nome como chave e ID como valor."""
    todasPessoas = Pessoa.buscar()
    return {i[1]: i[0] for i in todasPessoas} if todasPessoas else {}

def buscarPorId(idPessoa):
    """Busca uma pessoa pelo ID e retorna suas informações."""
    r = Pessoa.pesquisar_id(idPessoa)
    return {
        "idPessoa": r[0],
        "nome": r[1],
        "cpfCnpj": r[2],
        "dataNasc": r[3],
        "telefone": r[4],
        "email": r[5],
        "cargo": r[6],
    }

def atualizarPessoa(idPessoa, nome, cpfCnpj, dataNasc, telefone, email, cargo):
    """Atualiza os dados de uma pessoa existente no banco de dados."""
    pessoaModel = Pessoa()
    return pessoaModel.atualizar(idPessoa, nome, cpfCnpj, dataNasc, telefone, email, cargo)

def removerPessoa(idPessoa):
    """Remove uma pessoa do banco de dados pelo ID."""
    return Pessoa.deletar(idPessoa)