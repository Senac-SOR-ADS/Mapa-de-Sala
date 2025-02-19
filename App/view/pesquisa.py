from PyQt5.QtWidgets import QWidget, QStackedWidget, QDateEdit, QGridLayout
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate, pyqtSlot

from App.controller.curso import listarCurso
from App.controller.sala import listarSala

from .editarReservaUnitaria import ReservaUnitaria
from .cardPesquisa import CardPesquisa

class TelaPesquisa(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/pesquisa.ui',self)

        self.dicionarioCursos = listarCurso()
        self.dicionarioDeSala = listarSala()

        self.dataInicio = self.findChild(QDateEdit, 'dataInicio') 
        self.dataFim = self.findChild(QDateEdit, 'dataFim')
        self.dataInicio.setCalendarPopup(True)
        self.dataFim.setCalendarPopup(True)
        self.dataInicioMultiplo.setCalendarPopup(True)
        self.dataFimMultiplo.setCalendarPopup(True)

        self.dataInicio.setDisplayFormat('dd/MM/yyyy')
        self.dataInicio.setDate(QDate.currentDate())
        self.dataFim.setDisplayFormat('dd/MM/yyyy')
        self.dataFim.setDate(QDate.currentDate())
        self.setDataMinima()
        self.popularTela()

        self.dataInicio.dateChanged.connect(self.setDataMinima)
        
        self.checks.setStyleSheet("""
                QCheckBox::indicator {
                    width: 30px;
                    height: 30px;
                }
                QCheckBox::indicator:unchecked {
                    image: url("App/view/ui/icones/checkBox.png");
                }
                QCheckBox::indicator:checked {
                    image: url("App/view/ui/icones/iconCheckBoxAtivo.png");
                }
            """)

        self.stackReservas: QStackedWidget
        self.reservaMultipla: QWidget

        self.btnTrocarOfetaMultipla.clicked.connect(lambda: self.trocarTela(self.reservaMultipla))
        self.btnTrocarOfetaUnitaria.clicked.connect(lambda: self.trocarTela(self.reservaUnica))

    @pyqtSlot()
    def on_btnPesquisar_clicked(self):
        self.popularScrollArea()

    def trocarTela(self, tela:QWidget):
        self.stackReservas.setCurrentWidget(tela)

    def setDataMinima(self):
        data = self.dataInicio.date()
        self.dataFim.setMinimumDate(data)

    def comboboxOferta(self):
        ofertas = self.dicionarioCursos.keys()
        self.campoOferta.addItems(ofertas)

    def comboboxSala(self):
        salas = self.dicionarioDeSala.keys()
        self.campoSala.addItems(salas)

    def popularTela(self):
        self.comboboxOferta()
        self.comboboxSala()

    def criarPopUp(self):
        tela = ReservaUnitaria()
        if tela.exec_():
            pass

    def popularScrollArea(self):
        self.btnPesquisar.setEnabled(False)

        container = QWidget()
        grid = QGridLayout(container)
        card = CardPesquisa
        self.gridContainer.setWidget(container)
        max_colunas = 6
        coluna = 0
        linha = 0
        # o numero do range será os itens da retorno da função de consulta
        for i in range(1200):
            grid.addWidget(card(), linha, coluna)
            coluna += 1
            if coluna == max_colunas:
                coluna = 0
                linha += 1
        self.btnPesquisar.setEnabled(True)

##########Tela Multipla########################


############################################
        


###########NOME DOS BTNS E INPUTS ##############

        #btnEditar = btnEditar
        #btnExcluir = btnExcluir
        #inputOferta = campoOferta
        #inpuPeriodo = campoPeriodo
        #inputSala = campoSala
        #inputDataInicio = dataInicio
        #inputDataFim = dataFim