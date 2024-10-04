from PyQt5.QtWidgets import QApplication
from controller.login import LoginController
from controller.home import HomeController
from controller.sala import SalaController

if __name__ == "__main__":
    app = QApplication([])
    # login = LoginController()
    
    # if login.exec_():
    #     main = HomeController()
    sala = SalaController()
    app.exec_()
      