from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

class ConfigurarTela(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/telaConfiguracoes.ui', self)
