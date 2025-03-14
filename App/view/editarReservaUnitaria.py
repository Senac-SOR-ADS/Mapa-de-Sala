from PyQt5.QtWidgets import QDialog, QDateEdit, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QDate, QTime, pyqtSlot
from App.controller.pessoa import buscarPessoas
from App.controller.sala import listarSala
from App.controller.reserva import getReserva

class ReservaUnitaria(QDialog):
    def __init__(self, idReserva, dataReserva):
        super().__init__()
        loadUi('App/view/ui/editarReservaUnitaria.ui',self)
        self.dadosReserva = getReserva(idReserva)
        self.dadosConsultados = {
            'pessoas': buscarPessoas(),
            'salas': listarSala(),
            'pessoaAtual': self.dadosReserva[2],
            'salaAtual': self.dadosReserva[4],
        }

        self.dataReserva = dataReserva
        self.dadosReserva = getReserva(idReserva)
        self.inicio = self.getHoraFormatada(self.dadosReserva[6])
        self.fim = self.getHoraFormatada(self.dadosReserva[7])
        self.observacao = self.dadosReserva[9]

        self.diaInicio.setCalendarPopup(True)
        self.diaInicio.setDisplayFormat('dd/MM/yyyy')
        self.diaInicio.setMinimumDate(QDate.currentDate())
        self.inicioCurso.timeChanged.connect(self.setMinimoHoraFim)

        self.popularJanela(self.inicio, self.fim, self.observacao)
        self.setDataReserva()

        print("id da reserva", idReserva)
        print('pessoaAtual', self.dadosReserva[2])
        print(self.dadosConsultados['pessoas'])

    def popularJanela(self, horaInicio, horaFim, observacao):
        self.comboBoxPessoa()
        self.comboBoxSala()
        self.setHoraInicio(horaInicio)
        self.setHoraFim(horaFim)
        self.setMinimoHoraFim()
        self.setObservacao(observacao)
        
    def get_indice_pessoa_atual(self):
        pessoas = self.dadosConsultados['pessoas']
        for i in range(len(pessoas.keys())):
            if list(pessoas.keys())[i] == self.dadosConsultados['pessoaAtual']:
                # print(f'pessoa atual: ID({i})- Nome({list(pessoas.keys())[i]})')
                return i
        return 0
    
    def get_indice_sala_atual(self):
        salas = self.dadosConsultados['salas']
        salaAtual = self.dadosConsultados['salaAtual']
        indice = list(salas.values()).index(salaAtual)
        return indice

    def comboBoxPessoa(self):
        """Busca as pessoas no banco e popula o comboBox."""
        pessoas = self.dadosConsultados['pessoas'] #buscarPessoas()
        self.nomeDocente.clear()
        self.nomeDocente.addItems(pessoas.values())

        pessoa_atual = self.get_indice_pessoa_atual()
        self.nomeDocente.setCurrentIndex(pessoa_atual)

        # print(f'indice pessoa atual: {pessoa_atual}')

    def comboBoxSala(self):
        """Busca as salas no banco e popula o comboBox."""
        salas = self.dadosConsultados['salas']
        self.salaReserva.clear()
        self.salaReserva.addItems(salas.keys())

        sala_atual = self.get_indice_sala_atual()
        self.salaReserva.setCurrentIndex(sala_atual)

    def setDataReserva(self):
        self.diaInicio.setDate(self.dataReserva)
 
    def getHoraFormatada(self, horaTimedelta):
        time = QTime()
        stringHoras = str(horaTimedelta)
        hora = int(stringHoras.split(':')[0])
        minuto = int(stringHoras.split(':')[1])
        time.setHMS(hora, minuto, 0)
        return time
   
    def setHoraInicio(self, horas):
        self.inicioCurso.setTime(horas)
 
    def setHoraFim(self, horas):
        self.fimCurso.setTime(horas)
 
    def setMinimoHoraFim(self):
        time = self.inicioCurso.time()
        self.fimCurso.setMinimumTime(time)
   
    def setObservacao(self, txt):
        self.observacaoReserva.setText(txt)

    @pyqtSlot()
    def on_btnEditarReserva_clicked(self):
        docente = self.nomeDocente.currentText()
