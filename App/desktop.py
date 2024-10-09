from PyQt5.QtWidgets import QApplication
from App.view.login import LoginInterface
from App.view.home import HomePrincipal


app = QApplication([])
login = LoginInterface()

if login.exec_():
    main = HomePrincipal()
app.exec_()
    