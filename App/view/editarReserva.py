from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

class EditarReserva(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/editarReserva.ui',self)
        
        #btn editar reserva = btnEditarReserva