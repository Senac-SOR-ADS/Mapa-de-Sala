from PyQt5.QtWidgets import QApplication
from App.view.login import LoginInterface
from App.view.home import HomePrincipal
from App.view.cadastrarCurso import CadastrarCurso


app = QApplication([])
# login = LoginInterface()

# if login.exec_():
#     main = HomePrincipal()
main = CadastrarCurso()
main.show()
app.exec_()
    