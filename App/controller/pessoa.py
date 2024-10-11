from App.model.pessoa import Pessoa

def cadastrarPessoa(nome, cpfCnpj, dataNasc, telefone, email, cargo):
    pessoaModel = Pessoa()
    return pessoaModel.cadastrar(nome,
                          cpfCnpj,
                          dataNasc,
                          telefone,
                          email,
                          cargo)
