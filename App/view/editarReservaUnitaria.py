from PyQt5.QtWidgets import QDialog, QDateEdit, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt

from App.model.reserva import Reserva
 
class ReservaUnitaria(QDialog):
    def __init__(self, idReserva):
        super().__init__()
        loadUi('App/view/ui/editarReservaUnitaria.ui',self)
        self.popularCampos(idReserva)

    def popularCampos(self, idReserva):
        Reserva.retornar_uma_reserva(idReserva)