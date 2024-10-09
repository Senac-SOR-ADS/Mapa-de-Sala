from model.login import Login
from view.login import LoginInterface


class LoginController(LoginInterface):
    def __init__(self):
        super().__init__()
        self.show()

        self.btnEntrar.clicked.connect(self.validarLogin)

    def validarLogin(self):
        emailRetornado, senhaRetornada = self.getEmailSenha()
        login = Login(email=emailRetornado, senha=senhaRetornada)
        if login.validarLogin():
            self.accept()
        else:
            self.dadosInvalidos()