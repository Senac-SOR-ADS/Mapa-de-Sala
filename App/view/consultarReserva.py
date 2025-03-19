from PyQt5.QtWidgets import QWidget, QDateEdit
from PyQt5.QtCore import QDate
from PyQt5.uic import loadUi

class ConsultarReserva(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/consultarReserva.ui', self)

        self.buscarData = self.findChild(QDateEdit, 'buscarData') 
        self.dataRelatorio = self.findChild(QDateEdit, 'dataRelatorio')

        self.buscarData.setCalendarPopup(True)
        self.buscarData.setDisplayFormat('dd/MM/yyyy')
        self.buscarData.setDate(QDate.currentDate())

        self.dataRelatorio.setCalendarPopup(True)
        self.dataRelatorio.setDisplayFormat('dd/MM/yyyy')
        self.dataRelatorio.setDate(QDate.currentDate())
        
        self.setDataMinima()

        self.buscarData.dateChanged.connect(self.setDataMinima)

    def setDataMinima(self):
        """Define a data mínima de término da reserva"""
        primeiroDia = self.buscarData.date()
        self.buscarData.setMinimumDate(primeiroDia)
