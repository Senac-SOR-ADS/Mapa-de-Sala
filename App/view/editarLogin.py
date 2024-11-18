from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

class EditarLogin(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/editarLogin.ui',self)
        
        #btn editar login = btnEditarLogin