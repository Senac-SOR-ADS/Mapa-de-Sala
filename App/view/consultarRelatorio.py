from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi

class ConsultarRelatorio(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/consultarRelatorio.ui', self)
