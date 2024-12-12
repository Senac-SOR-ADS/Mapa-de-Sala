from PyQt5.QtWidgets import QWidget, QDateEdit
from PyQt5.QtCore import QDate
from PyQt5.uic import loadUi

class EditarReserva(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/editarReserva.ui',self)
        
        #btn editar reserva = btnEditarReserva

        self.diaInicio = self.findChild(QDateEdit, 'diaInicio') 
        self.diaFim = self.findChild(QDateEdit, 'diaFim')

        self.diaInicio.setCalendarPopup(True)
        self.diaInicio.setDisplayFormat('dd/MM/yyyy')
        self.diaInicio.setDate(QDate.currentDate())

        self.diaFim.setCalendarPopup(True)
        self.diaFim.setDisplayFormat('dd/MM/yyyy')
        self.diaFim.setDate(QDate.currentDate()) 