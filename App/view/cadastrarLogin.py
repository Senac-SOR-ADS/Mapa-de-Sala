from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi


class CadastroLogin(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/cadastroLogin.ui',self)
        
    #nome btn e inputs
    
    #input Email = email
    #input Senha = senha
    #btn cadastroLogin = btnCdastrarLogin
    #checkbox sla = nivelAcesso
    
        
        