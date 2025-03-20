from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QUrl
from os.path import join, dirname, realpath
from PyQt5.QtGui import QPixmap
from App.model.reserva import Reserva
from .telaConfirmacao import TelaConfirmacao

 
class CardPesquisa(QWidget):
    CURRENT_DIR = dirname(realpath(__file__))

    def __init__(self, id_reserva, sala, curso, cod_oferta, data, horario):
        super().__init__()
        loadUi('App/view/ui/cardPesquisa.ui',self)
        self.idReserva = id_reserva

        cssFile = join(self.CURRENT_DIR, f"./ui/css/cards/{horario.lower()}.css")
        with open(cssFile, 'r') as css:
            self.setStyleSheet(css.read())
        icone = join(self.CURRENT_DIR, f"./ui/icones/icon{horario}.png")
        self.iconePeriodo.setPixmap(QPixmap(icone))

        self.label_6.setText(data.strftime("%d/%m/%Y"))
        self.label_8.setText(f"{cod_oferta} - {curso}")
        self.label_9.setText(sala)

        self.btnExcluir.clicked.connect(self.excluirReserva)

    def excluirReserva(self):
        confirmacao = TelaConfirmacao("Deseja mesmo excluir essa reserva?", '', "Sim", False)
        if confirmacao.exec_():
            Reserva.deletar(self.idReserva)
            self.deleteLater()