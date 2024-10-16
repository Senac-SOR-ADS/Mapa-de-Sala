from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtCore import pyqtSlot



from App.controller.login import validarLogin


class LoginInterface(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/interfaceLogin.ui',self)
        # Remove a barra de título e as bordas da janela
        self.setWindowFlags(Qt.FramelessWindowHint)
        # Define a janela como transparente
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.btnMenuBar.clicked.connect(self.showMenu)

        # self.btnEntrar.clicked.connect(self.validarLogin)

    def showMenu(self):
        # Cria o menu suspenso
        self.menu = QMenu(self)
        
        # Adiciona ação "Minimizar"
        minimize_action = self.menu.addAction("Minimizar")
        minimize_action.triggered.connect(self.showMinimized)
        
        # Adiciona ação "Sair"
        exit_action = self.menu.addAction("Sair")
        exit_action.triggered.connect(self.closeApp)
        
        # Exibe o menu suspenso abaixo do botão de menu
        self.menu.exec_(self.btnMenuBar.mapToGlobal(self.btnMenuBar.rect().bottomLeft()))

    def closeApp(self):
        # Fecha a aplicação
        self.close()

    def getEmailSenha(self):
        email = self.inputEmail.text().strip()
        senha = self.inputSenha.text()
        return (email, senha)        

    def validandoDados(self):
        self.respostaLoginLogando.setText('LOGANDO...')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.respostaLoginLogando))

    def dadosInvalidos(self):
        texto = 'DADOS INCOMPLETOS.'
        self.respostaLoginDadosIncompleto.setText(texto)
        QTimer.singleShot(2000, lambda: self.limparCampos(self.respostaLoginDadosIncompleto))

    @pyqtSlot()
    def on_btnEntrar_clicked(self):
        campos = self.getEmailSenha()
        if validarLogin(campos[0], campos[1]):
            self.validandoDados()
            self.accept()
        else:
            self.dadosInvalidos()

    def limparCampos(self, campo):
        campo.clear()


if __name__ == "__main__":
    app = QApplication([])
    widget = LoginInterface()
    widget.show()
    app.exec_()
