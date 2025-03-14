from PyQt5.QtWidgets import QDialog, QDateEdit, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from App.controller.pessoa import buscarPessoas
from App.controller.sala import listarSala
from App.controller.reserva import getReserva

class ReservaUnitaria(QDialog):
    def __init__(self, idReserva):
        super().__init__()
        loadUi('App/view/ui/editarReservaUnitaria.ui',self)
        self.dadosReserva = getReserva(idReserva)
        self.dadosConsultados = {
            'pessoas': buscarPessoas(),
            'salas': listarSala(),
            'pessoaAtual': self.dadosReserva[2],
            'salaAtual': self.dadosReserva[4],
        }

        print("id da reserva", idReserva)
        print('pessoaAtual', self.dadosReserva[2])
        print(self.dadosConsultados['pessoas'])
        
        self.comboBoxPessoa()
        self.comboBoxSala()
    
    def get_indice_pessoa_atual(self):
        pessoas = self.dadosConsultados['pessoas']
        for i in range(len(pessoas.keys())):
            if list(pessoas.values())[i] == self.dadosConsultados['pessoaAtual']:
                print(f'pessoa atual: ID({i})- Nome({list(pessoas.keys())[i]})')
                return i
        return 0
    
    def get_indice_sala_atual(self):
        salas = self.dadosConsultados['salas']
        salaAtual = self.dadosConsultados['salaAtual']
        indice = list(salas.values()).index(salaAtual)
        return indice
        # for i in range(len(salas.values())):
        #     if list(salas.values())[i] == salaAtual:
        #         return i
        # return 0

    def comboBoxPessoa(self):
        """Busca as pessoas no banco e popula o comboBox."""
        pessoas = self.dadosConsultados['pessoas'] #buscarPessoas()
        self.nomeDocente.clear()
        self.nomeDocente.addItems(pessoas.values())
        # print('*'*50)
        # print(f'pessoas ADD: {pessoas.keys()}')
        # print('*'*50)

        # pessoa_atual = self.get_indice_pessoa_atual()
        # self.nomeDocente.setCurrentIndex(pessoa_atual)
        # print(f'indice pessoa atual: {pessoa_atual}')
        # print(f'pessoa selecionada: {self.nomeDocente.currentIndex()}')

    def comboBoxSala(self):
        """Busca as salas no banco e popula o comboBox."""
        salas = self.dadosConsultados['salas']
        self.salaReserva.clear()
        self.salaReserva.addItems(salas.keys())

        sala_atual = self.get_indice_sala_atual()
        self.salaReserva.setCurrentIndex(sala_atual)