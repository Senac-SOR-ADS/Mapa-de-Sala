from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from App.controller.login import listarLogins, buscarLoginId, atualizarCadastro
from App.controller.utils import validarInputs
 
class EditarLogin(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/editarLogin.ui',self)
       
        #btn editar login = btnEditarLogin
        self.dicionarioLogins = listarLogins()
        self.popularJanela()
        self.alterarLogin.currentIndexChanged.connect(self.popularCampos)
        self.btnMostrarSenha.clicked.connect(self.mostrarSenha)
 
    #Função para mudar visibilidade da senha
    def mostrarSenha(self):
        if self.senha.echoMode():
           self.senha.setEchoMode(self.senha.EchoMode.Normal)
           self.btnMostrarSenha.setStyleSheet('''
                                              #btnMostrarSenha {
                                                icon: url("App/view/ui/icones/iconOlhoFechado.png");    
                                              }''')
        else:
            self.senha.setEchoMode(self.senha.EchoMode.Password)
            self.btnMostrarSenha.setStyleSheet('''
                                              #btnMostrarSenha {
                                                icon: url("App/view/ui/icones/iconOlhoAberto.png");  
                                              }''')
 
    @pyqtSlot()
    def on_btnEditarLogin_clicked(self):
        dados = self.getValores()
        if validarInputs(dados[:-1]):
            atualizarCadastro(dados[0], dados[1], dados[2], dados[3])
 
    def popularJanela(self):
        self.comboboxLogin()
        self.popularCampos()
 
    def comboboxLogin(self):
        logins = self.dicionarioLogins.keys()
        self.alterarLogin.addItems(logins)
 
    def popularCampos(self):
        key = self.getKey()
        dados = buscarLoginId(key)
        self.email.setText(dados.get('email'))
        self.setNivelAcesso()
 
    def getKey(self):
        nome = self.alterarLogin.currentText()
        key = self.dicionarioLogins.get(nome)
        return key
   
    def getValores(self):
        email = self.email.text()
        senha = self.senha.text()
        nivelAcesso = self.nivelAcesso.currentText()
        nome = self.alterarLogin.currentText()
        idLogin = self.dicionarioLogins.get(nome)
 
        return (idLogin, email, nivelAcesso, senha)
   
    def setNivelAcesso(self):
        key = self.getKey()
        dados = buscarLoginId(key)
        self.nivelAcesso.setCurrentText(dados.get('nivelAcesso'))