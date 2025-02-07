from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

class TelaPesquisa(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/pesquisa.ui',self)

        self.dataInicio.setCalendarPopup(True)
        self.dataFim.setCalendarPopup(True)


###########NOME DOS BTNS E INPUTS ##############

        #btnEditar = btnEditar
        #btnExcluir = btnExcluir
        #inputOferta = campoOferta
        #inpuPeriodo = campoPeriodo
        #inputSala = campoSala
        #inputDataInicio = dataInicio
        #inputDataFim = dataFim