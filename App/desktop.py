from PyQt5.QtWidgets import QApplication
from App.view.login import LoginInterface
from App.view.home import HomePrincipal
from App.view.cadastroPessoas import cadastroPessoas


app = QApplication([])
# login = LoginInterface()

# if login.exec_():
#     main = HomePrincipal()
#     main.show()

cadaPessoa = cadastroPessoas()
cadaPessoa.show()
app.exec_()
    