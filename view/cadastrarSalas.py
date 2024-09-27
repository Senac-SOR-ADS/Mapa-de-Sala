from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class CadastrarSalas(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('view/ui/cadastroSalas.ui',self)

if __name__ == "__main__":
    app = QApplication([])
    widget = CadastrarSalas()
    widget.show()
    app.exec_()