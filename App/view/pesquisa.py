from PyQt5.QtWidgets import QWidget, QStackedWidget
from PyQt5.uic import loadUi

class TelaPesquisa(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/pesquisa.ui',self)

        self.dataInicio.setCalendarPopup(True)
        self.dataFim.setCalendarPopup(True)

        self.stackReservas: QStackedWidget
        self.reservaMultipla: QWidget

        self.teste.clicked.connect(self.stackReservas.setCurrentWidget(self.reservaMultipla))
        


###########NOME DOS BTNS E INPUTS ##############

        #btnEditar = btnEditar
        #btnExcluir = btnExcluir
        #inputOferta = campoOferta
        #inpuPeriodo = campoPeriodo
        #inputSala = campoSala
        #inputDataInicio = dataInicio
        #inputDataFim = dataFim