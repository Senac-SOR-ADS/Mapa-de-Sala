from App.model.login import Login

# =================== validar ===================
def validarLogin(email, senha):
    login = Login(email, senha)
    if login.validarLogin():
        return True
    else:
        return False

# =================== cadastrar ===================
def cadastrarLogin(idPessoa, cpf_cnpj, email, cargo):
    """Cadastra o login de um usuário associado à pessoa no banco de dados."""
    login_model = Login()   
    return login_model.cadastrar(idPessoa, cpf_cnpj, email, cargo)

# =================== atualizar ===================
def atualizarCadastro(idLogin, novoEmail, novoCargo):
    """Atualiza o email e o cargo de um usuário."""
    try:
        login_model = Login()
        if login_model.atualizar(idLogin, novoEmail, novoCargo):
            return {"success": "Email e cargo atualizados com sucesso."}
        return {"error": "Falha ao atualizar email e cargo."}
    
    except Exception as e:
        return {"error": f"Erro: {str(e)}"}

# =================== buscar Id ===================
def buscarLoginId(idPessoa):
    """Busca uma pessoa pelo ID e retorna suas informações de login."""
    if not isinstance(idPessoa, int):
        return {"error": "ID inválido. Deve ser um número inteiro."}
    try:
        resultado = Login.pesquisar_id(idPessoa)
        if not resultado or len(resultado) < 5:
            return {"error": "Login não encontrado"}

        return {
            "idLogin": resultado[0],
            "idPessoa": resultado[1],
            "email": resultado[2],
            "senha": resultado[3],
            "nivelAcesso": resultado[4],
        }
    except Exception as e:
        return {"error": f"Erro ao buscar login: {e}"}

# =================== Remove ===================
def removerLogin(idLogin):
    """Remove um login do banco de dados associado ao ID do login."""
    login_model = Login()
    return login_model.deletar(idLogin)
