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
        container = QWidget()
        grid = QGridLayout(container)
        card = CardPesquisa
        self.gridContainer.setWidget(container)
        import time
        ti = time.time()

        for linha in range(400):
            for coluna in range(6):
                grid.addWidget(card(), linha, coluna)
        tf = time.time()
        tempo_total = tf - ti
        print(f"Tempo de execução: {tempo_total:.6f} segundos")
        print('card chamado')

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