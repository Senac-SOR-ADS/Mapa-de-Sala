from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

class EditarCurso(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/editarCurso.ui',self)
        
        # btn editar curso = btnEditarCurso