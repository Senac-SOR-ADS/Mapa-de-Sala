
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer


class LoginInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('interfaceLogin.ui',self)
        
        # Remove a barra de título e as bordas da janela
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Define a janela como transparente
        self.setAttribute(Qt.WA_TranslucentBackground)

        #Conectando os botões:
        self.btnEntrar.clicked.connect(self.getEmailSenha)


    def getEmailSenha(self):
        email = self.inputEmail.text()
        senha = self.inputSenha.text()

        if (email != '' and senha !=''):
            print(email, senha)
        else:
            texto = 'Dados incompletos'
            self.respostaLogin.setText(texto)
            QTimer.singleShot(2000, lambda: self.limparCampos(self.respostaLogin))
            


        self.limparCampos(self.inputEmail)
        self.limparCampos(self.inputSenha)
    



    def limparCampos(self, campo):
        campo.clear()






if __name__ == "__main__":
    app = QApplication([])
    widget = LoginInterface()
    widget.show()

    app.exec_()


