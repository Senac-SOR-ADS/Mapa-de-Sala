from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

class EditarPessoas(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/editarPessoa.ui',self)
        
        # btn editar pessoas = btnEditar