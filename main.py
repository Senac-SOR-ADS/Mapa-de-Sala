from PyQt5.QtWidgets import QApplication
from controller.login import LoginController
from controller.home import HomeController

if __name__ == "__main__":
    app = QApplication([])
    login = LoginController()
    
    if login.exec_():
        # Implementar o controlador para a mainWindow
        main = HomeController()
        app.exec_()
      