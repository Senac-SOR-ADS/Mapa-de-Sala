from App.model.pessoa import Pessoa

def cadastrarPessoa(nome, cpfCnpj, dataNasc, telefone, email, cargo):
    pessoaModel = Pessoa()
    return pessoaModel.cadastrar(nome,
                          cpfCnpj,
                          modificarData(dataNasc),
                          telefone,
                          email,
                          cargo)

def modificarData(dataNasc):
    data = dataNasc.split('/')
    return f'{data[2]}-{data[1]}-{data[0]}'


def buscaPessoas():
    todasPessoas = Pessoa.buscarPessoas()
    listaPessoas = {i[1]:i[0] for i in todasPessoas}
    return listaPessoas