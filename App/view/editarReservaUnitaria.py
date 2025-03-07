from PyQt5.QtWidgets import QDialog, QDateEdit, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from App.controller.sala import listarSala
from App.controller.pessoa import buscarPessoas

from App.model.reserva import Reserva
 
class ReservaUnitaria(QDialog):
    def __init__(self, idReserva):
        super().__init__()
        loadUi('App/view/ui/editarReservaUnitaria.ui',self)
        self.dadosConsultados = {
            'pessoas': buscarPessoas(),
            'salas': listarSala(),
        }

        print("id da reserva", idReserva)
        self.popularJanela()

    def popularJanela(self):
        self.comboBoxPessoa()
        self.comboBoxSala()

    def comboBoxPessoa(self):
        """Busca as pessoas no banco e popula o comboBox."""
        pessoas = self.dadosConsultados['pessoas'] #buscarPessoas()
        self.nomeDocente.clear()
        self.nomeDocente.addItems(pessoas.keys())

    def comboBoxSala(self):
        """Busca as salas no banco e popula o comboBox."""
        salas = self.dadosConsultados['salas'] #listarSala()
        self.salaReserva.clear()
        self.salaReserva.addItems(salas.keys())