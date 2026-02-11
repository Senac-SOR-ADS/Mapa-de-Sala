from PyQt5.QtWidgets import QWidget, QDateEdit
from PyQt5.QtCore import QDate, pyqtSlot
from PyQt5.uic import loadUi
from App.controller.relatorio import relatorioSalaLivre, gerarRelatorio
from App.controller.utils import modificarData

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

    @pyqtSlot()
    def on_salasLivres_clicked(self):
        dia = modificarData(self.buscarData.text().strip() )
        h_inicio = self.horaInicio.text()
        h_fim = self.horaFim.text()
        relatorioSalaLivre(dia, h_inicio, h_fim)
    
    @pyqtSlot()
    def on_buscarRelatorios_clicked(self):
        dia = modificarData(self.dataRelatorio.text().strip() )
        gerarRelatorio(dia)