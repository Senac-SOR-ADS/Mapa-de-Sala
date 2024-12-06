from PyQt5.QtWidgets import QApplication
from App.view.login import LoginInterface
from App.view.home import HomePrincipal
from App.controller.login import pegarUsuarioLogado


app = QApplication([])
login = LoginInterface()

while pegarUsuarioLogado()['id_login'] == None:
    if login.exec_():
        main = HomePrincipal()
        main.show()
        app.exec_()
    else:
        break