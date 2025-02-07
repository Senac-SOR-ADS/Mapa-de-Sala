from PyQt5.QtWidgets import QDialog, QMenu
from PyQt5.QtCore import Qt, QTimer, QPoint
from PyQt5.QtCore import pyqtSlot
import PyQt5.QtCore
from .feedback import Feedback
from PyQt5.uic import loadUi
from os import path
import os
from PyQt5 import QtMultimedia

 
from App.controller.login import validarLogin
 
#respostasErros = aviso erros
 
class LoginInterface(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/Login.ui',self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
 
        self.old_pos = None
        self.inputEmail.setFocus()
 
        # Faz a conexão do botão MenuBar
        self.btnMenuBar.clicked.connect(self.showMenu)
        self.btnMostrarSenha.clicked.connect(self.mostrarSenha)
        # self.btnEntrar.clicked.connect(self.validarLogin)
 
    def mostrarSenha(self):
        if self.inputSenha.echoMode() == 2:
           self.inputSenha.setEchoMode(self.inputSenha.EchoMode.Normal)
           self.btnMostrarSenha.setStyleSheet('''
                                              #btnMostrarSenha {
                                                icon: url("App/view/ui/icones/iconOlhoFechado.png");    
                                              }''')
        else:
            self.inputSenha.setEchoMode(self.inputSenha.EchoMode.Password)
            self.btnMostrarSenha.setStyleSheet('''
                                              #btnMostrarSenha {
                                                icon: url("App/view/ui/icones/iconOlhoAberto.png");  
                                              }''')
 
 
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
 
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Captura a posição inicial do mouse
            self.old_pos = event.globalPos()
 
    def mouseMoveEvent(self, event):
        if self.old_pos:
            # Calcula o deslocamento do mouse
            delta = QPoint(event.globalPos() - self.old_pos)
            # Move a janela pela diferença calculada
            self.move(self.x() + delta.x(), self.y() + delta.y())
            # Atualiza a posição do mouse
            self.old_pos = event.globalPos()
 
    def mouseReleaseEvent(self, event):
        # Libera a janela ao soltar o botão do mouse
        if event.button() == Qt.LeftButton:
            self.old_pos = None
 
    def getEmailSenha(self):
        email = self.inputEmail.text().strip()
        senha = self.inputSenha.text()
        return (email, senha)        
 
    # def validandoDados(self):
    #     # self.respostasErros.setText('LOGANDO...')
    #     QTimer.singleShot(2000, lambda: self.limparCampos(self.respostasErros))
 
    def dadosInvalidos(self):
        texto = 'DADOS INCOMPLETOS.'
        resposta = Feedback(False,
                            texto,
                            'Aviso!',
                            'algo deu errado, corrija as falhas e tente novamente')
        
        # resposta.mudarFoto("Validado")
        if resposta.exec_():
            print('erro')
       
       
 
    @pyqtSlot()
    def on_btnEntrar_clicked(self):
        campos = self.getEmailSenha()
        if validarLogin(campos[0], campos[1]):
            self.accept()
        else:
            self.dadosInvalidos()
 
    def limparCampos(self, campo):
        campo.clear()
 
 
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    widget = LoginInterface()
    widget.show()
    app.exec_()