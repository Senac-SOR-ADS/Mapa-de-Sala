from PyQt5.QtWidgets import QWidget, QStackedWidget, QDateEdit
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate

from App.controller.curso import listarCurso
from App.controller.sala import listarSala

from .editarReservaUnitaria import ReservaUnitaria
from .telaConfirmacao import TelaConfirmacao

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

        self.dataInicio.setDisplayFormat('dd/MM/yyyy')
        self.dataInicio.setDate(QDate.currentDate())
        self.dataFim.setDisplayFormat('dd/MM/yyyy')
        self.dataFim.setDate(QDate.currentDate())
        self.setDataMinima()
        self.popularTela()

        self.dataInicio.dateChanged.connect(self.setDataMinima)

        self.stackReservas: QStackedWidget
        self.reservaMultipla: QWidget

        self.btnTrocarOfetaMultipla.clicked.connect(lambda: self.trocarTela(self.reservaMultipla))
        self.btnTrocarOfetaUnitaria.clicked.connect(lambda: self.trocarTela(self.reservaUnica))

        self.btnEditar.clicked.connect(self.criarPopUp)
        self.btnExcluir.clicked.connect(self.excluirReserva)


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

    def excluirReserva(self):
        confirmacao = TelaConfirmacao("Tem certeza que deseja excluir?", '', "Sim", False)
        if confirmacao.exec_():
            print('excluido')
        print('Não excluido')

        


###########NOME DOS BTNS E INPUTS ##############

        #btnEditar = btnEditar
        #btnExcluir = btnExcluir
        #inputOferta = campoOferta
        #inpuPeriodo = campoPeriodo
        #inputSala = campoSala
        #inputDataInicio = dataInicio
        #inputDataFim = dataFim