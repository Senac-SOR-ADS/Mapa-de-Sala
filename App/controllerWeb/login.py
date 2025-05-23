from flask import session
from App.model.login import Login
from App.model.logger import logger

# =================== validar ===================
def validarLogin(email: str, senha: str) -> bool:
    try:
        login = Login(email, senha)

        if not login.validarLogin():
            return False

        session.permanent = True
        session["usuario"] = {
            "id_login": login.getIdLogin(),
            "id_pessoa": login.getIdPessoa(),
            "email": login.getEmail(),
            "nivel_acesso": login.getNivelAcesso(),
        }

        logger.success("Login realizado para o usuário %s", email)
        return True
    except Exception as e:
        logger.error("Erro ao validar login: %s", e, exc_info=True)
        return False

# ------------------------------------------------------------------------------
# Obtém informações do usuário logado
# ------------------------------------------------------------------------------

def pegarUsuarioLogado() -> dict | None:
    return session.get("usuario")

def pegar_acesso():
    usuario = session.get('usuario')
    return (usuario, session.get('nivel_acesso')) if usuario else (None, None)

# =========== Remover usuário logado ============
def removerUsuarioLogado():
    session.pop("usuario", None)

# =================== cadastrar ===================
def cadastrarLogin(idPessoa, cpf_cnpj, email, cargo):
    """Cadastra o login de um usuário associado à pessoa no banco de dados."""
    login_model = Login()
    try:
        sucesso = login_model.cadastrar(idPessoa, cpf_cnpj, email, cargo)
        if sucesso:
            logger.info("Cadastro de login realizado para o usuário %s", email)
            return {"success": "Cadastro realizado com sucesso."}
        return {"error": "Erro ao realizar cadastro. Tente novamente."}
    except Exception as e:
        logger.error("Erro ao cadastrar login para o usuário %s: %s", email, str(e))
        return {"error": f"Ocorreu um erro inesperado: {str(e)}"}

# =================== atualizar  ===================
def atualizarCadastro(idLogin, novoEmail=None, novoCargo=None, novaSenha=None):
    """Atualiza o email, nível de acesso (baseado no cargo) ou apenas a senha de um usuário."""
    try:
        login_model = Login()
        
        if not novoEmail and not novoCargo and not novaSenha:
            return {"error": "Nenhum dado para atualizar."}
        
        sucesso = login_model.atualizarWEB(idLogin, novoEmail, novoCargo, novaSenha)
        
        if sucesso:
            logger.info("Cadastro atualizado com sucesso para o ID de login %s", idLogin)
            return {"success": "Cadastro atualizado com sucesso."}
        return {"error": "Erro ao atualizar o cadastro. Tente novamente."}
    except Exception as e:
        logger.error("Erro ao atualizar o cadastro para o ID de login %s: %s", idLogin, str(e))
        return {"error": f"Ocorreu um erro inesperado: {str(e)}"}

# =================== listar ===================
def listarLogins() -> dict:
    try:
        logins = Login.buscar_todos()
        logins_dict = {login.getEmail(): login.getIdLogin() for login in logins}
        return logins_dict
    except Exception as e:
        logger.error("Erro ao listar logins: %s", str(e))
        return {"error": "Erro ao listar os logins."}

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
        logger.error("Erro ao buscar login para o ID %d: %s", idPessoa, str(e))
        return {"error": f"Erro ao buscar login: {str(e)}"}

# =================== Remove ===================
def removerLogin(idLogin):
    """Remove um login do banco de dados associado ao ID do login."""
    try:
        login_model = Login()
        sucesso = login_model.deletar(idLogin)
        if sucesso:
            logger.info("Login removido com sucesso para o ID %s", idLogin)
            return {"success": "Login removido com sucesso."}
        return {"error": "Erro ao remover o login. Tente novamente."}
    except Exception as e:
        logger.error("Erro ao remover login para o ID %s: %s", idLogin, str(e))
        return {"error": f"Erro ao remover login: {str(e)}"}
