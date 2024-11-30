from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

class EditarSala(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/editarSalas.ui',self)
        
        # btn editar sala = btnEditarSala