from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
 
 
class CadastroLogin(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/cadastroLogin.ui',self)
       
        self.btnMostrarSenha.clicked.connect(self.mostrarSenha)
       
    #nome btn e inputs
   
    #input Email = email
    #input Senha = senha
    #btn cadastroLogin = btnCdastrarLogin
    #checkbox sla = nivelAcesso
    #msgs de erro ou sucesso = respostas
   
    #Função para mudar visibilidade da senha
    def mostrarSenha(self):
        if self.senha.echoMode() == 2:
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