from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class TelaConflitos(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/telaConflitos.ui', self)