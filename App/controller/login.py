from App.model.login import Login


def validarLogin(email, senha):
    login = Login(email, senha)
    if login.validarLogin():
        return True
    return False