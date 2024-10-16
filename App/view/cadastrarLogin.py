from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt


class cadastroLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/cadastroLogin.ui',self)
        
    #nome btn e inputs
    
    #input Email = email
    #input Senha = senha
    #btn cadastroLogin = btnCdastrarLogin
    
        
        
        
        
if __name__ == "__main__":
    app = QApplication([])
    widget = cadastroLogin()
    widget.show()
    app.exec_()