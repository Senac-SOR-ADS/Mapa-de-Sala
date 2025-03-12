from PyQt5.QtWidgets import QWidget, QStackedWidget, QDateEdit, QGridLayout
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate, pyqtSlot

from App.controller.curso import listarCurso
from App.controller.sala import listarSala
from App.controller.reserva import verificarPesquisa

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


        self.dataInicioMultiplo.setDisplayFormat('dd/MM/yyyy')
        self.dataInicioMultiplo.setDate(QDate.currentDate())
        self.dataFimMultiplo.setDisplayFormat('dd/MM/yyyy')
        self.dataFimMultiplo.setDate(QDate.currentDate())

        self.dataInicioMultiplo = self.findChild(QDateEdit, 'dataInicioMultiplo')
        self.dataFimMultiplo = self.findChild(QDateEdit, 'dataFimMultiplo')

        self.setDataMinima()
        self.setDataDiaria()
        self.popularTela()

        self.dataInicio.dateChanged.connect(self.setDataMinima)
        self.dataInicioMultiplo.dateChanged.connect(self.setDataMinima)

        self.container_GRID = QWidget()
        self.grid = QGridLayout(self.container_GRID)
        self.gridContainer.setWidget(self.container_GRID)
        
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
        dados = self.getDados() 
        reservas = verificarPesquisa(dados)
        if reservas:
            self.popularScrollArea(reservas)
        else:
            print('não tem reseversa na pesquisa')

    def setDataDiaria(self):
        data = QDate.currentDate()
        self.dataInicioMultiplo.setMinimumDate(data)
        self.dataInicio.setMinimumDate(data)
    



    def trocarTela(self, tela:QWidget):
        self.setDataDiaria()
        self.stackReservas.setCurrentWidget(tela)

    def setDataMinima(self):
        data = self.dataInicio.date()
        self.dataFim.setMinimumDate(data)
        dataMultiplo = self.dataInicioMultiplo.date()
        self.dataFimMultiplo.setMinimumDate(dataMultiplo)


    def comboboxOferta(self):
        ofertas = self.dicionarioCursos.values()
        self.campoOferta.addItems(ofertas)
        self.campoOfertaMultipla.addItems(ofertas)

    def comboboxSala(self):
        salas = self.dicionarioDeSala.keys()
        self.campoSala.addItems(salas)

    def popularTela(self):
        self.comboboxOferta()
        self.comboboxSala()

    def definirPeriodo(self):
        if self.campoPeriodo.currentText() == 'Manha':
            horaInicio = '08:00:00'
            horaFim = '12:00:00'
            return horaInicio, horaFim
        if self.campoPeriodo.currentText() == 'Tarde':
            horaInicio = '13:00:00'
            horaFim = '18:00:00'
            return horaInicio, horaFim
        if self.campoPeriodo.currentText() == 'Noite':
            horaInicio = '19:00:00'
            horaFim = '22:00:00'
            return horaInicio, horaFim
   
    def getDados(self):
        index_oferta = self.campoOferta.currentIndex()
        oferta = None
        if index_oferta:
            oferta = list(self.dicionarioCursos.keys())[index_oferta-1]

        index_sala = self.campoSala.currentIndex()
        sala = None
        if index_sala:
            sala = list(self.dicionarioDeSala.values())[index_sala-1]
 
        index_periodo = self.campoPeriodo.currentIndex()
        horaInicio, horaFim = None, None
        if index_periodo:
            horaInicio, horaFim = self.definirPeriodo()
 
        dataInicio = self.dataInicio.date().toString('yyyy-MM-dd')
        dataFim = self.dataFim.date().toString('yyyy-MM-dd')
       
        dados = { 'oferta' : oferta,
                 'horaInicio' : horaInicio,
                 'horaFim' : horaFim,
                 'dataInicio' : dataInicio,
                 'dataFim' : dataFim,
                 'sala' : sala }
        print(dados)
        return dados

    def criarPopUp(self):
        tela = ReservaUnitaria()
        if tela.exec_():
            pass

    def popularScrollArea(self, lista_de_reservas: list):
        self.btnPesquisar.setEnabled(False)

        for card in self.grid.findChildren(QWidget):
            del card
            print('deletado')
        print('-' * 100)
        print(lista_de_reservas)
        print('-' * 100)

        max_colunas = 6
        coluna = 0
        linha = 0
        for reserva in lista_de_reservas:
            card = CardPesquisa(*reserva)
            self.grid.addWidget(card, linha, coluna)
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