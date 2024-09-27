from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class HomePrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('view/ui/interfaceHomeV1.ui',self)

if __name__ == "__main__":
    app = QApplication([])
    widget = HomePrincipal()
    widget.show()
    app.exec_()