from PyQt5.QtWidgets import QWidget, QStackedWidget, QDateEdit
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate, pyqtSlot

from App.controller.curso import listarCurso
from App.controller.sala import listarSala
from App.controller.reserva import verificarPesquisa

from .editarReservaUnitaria import ReservaUnitaria

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

        self.dataInicioMultiplo = self.findChild(QDateEdit, 'dataInicio') 
        self.dataFimMultiplo = self.findChild(QDateEdit, 'dataFim')

        self.setDataMinima()
        self.setDataDiaria()
        self.setDataDiariaMultiplo()
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

    def setDataDiaria(self):
        data = QDate.currentDate()
        self.dataInicio.setMinimumDate(data)
        self.dataInicioMultiplo.setMinimumDate(data)
    



    def trocarTela(self, tela:QWidget):
        self.stackReservas.setCurrentWidget(tela)

    def setDataMinima(self):
        data = self.dataInicio.date()
        self.dataFim.setMinimumDate(data)

    def comboboxOferta(self):
        ofertas = self.dicionarioCursos.keys()
        self.campoOferta.addItems(ofertas)
        self.campoOfertaMultiplo.addItems(ofertas)

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
   
 
    @pyqtSlot()
    def on_btnPesquisar_clicked(self):
        dados = self.getDados()
        reservas = verificarPesquisa(dados)
        print(reservas)
 
    def getDados(self):
        index_oferta = self.campoOferta.currentIndex()
        oferta = None
        if index_oferta:
            oferta = list(self.dicionarioCursos.values())[index_oferta-1]
 
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
        return dados

    def criarPopUp(self):
        tela = ReservaUnitaria()
        if tela.exec_():
            pass

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