from PyQt5.QtWidgets import QApplication
from App.view.login import LoginInterface
from App.view.home import HomePrincipal
from App.view.cadastrarArea import CadastrarArea


app = QApplication([])
# login = LoginInterface()

# if login.exec_():
    # main = HomePrincipal()
main = CadastrarArea()
main.show()
app.exec_()
    