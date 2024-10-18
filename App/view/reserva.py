from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer, pyqtSlot
from App.model.reserva import Reserva

from App.controller.curso import listarCursos
from App.controller.pessoa import buscaPessoas
from App.controller.sala import listarSala

from App.model.login import Login



class ReservaInterface(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/reserva.ui',self)
        self.popularJanela()

    def getDados(self)->dict:
        """Pegando o dados na interface e retornando os valores"""
        nomeDocenteResponsavel = self.nomeDocente.text().strip() 
        nomeSala = self.salaReserva.text().strip() 
        nomeCurso = self.cursoReserva.text().strip() 
        equipamentos = self.equipamentosReserva.text().strip() 
        inicio = self.inicioReserva.text().strip() 
        fim = self.fimReserva.text().strip() 
        observacao = self.observacaoReserva.text().strip() 
        
        dados = {"nomeDocente":nomeDocenteResponsavel, 
                 "nomeSala":nomeSala, 
                 "nomeCurso":nomeCurso,
                 "equipamentos":equipamentos,
                 "inicio":inicio,
                 "fim":fim,
                 "observações":observacao}
        return dados
    
    @pyqtSlot()
    def on_btnFazerReserva_clicked(self):
        info = self.getDados()
        idLogin = Login.getIdLogin()
        if Reserva(idLogin, info).fazer_reserva():
            print('ok')        
        
        
        
        

    def popularJanela(self):
        self.comboBoxCurso()
        self.comboBoxPessoa()
        self.comboBoxSala()

    def comboBoxCurso(self):
        curso = listarCursos().keys()
        self.cursoReserva.addItems(curso)

    def comboBoxPessoa(self):
        pessoa = buscaPessoas().keys()
        self.nomeDocente.addItems(pessoa)

    def comboBoxSala(self):
        sala = listarSala().keys()
        self.salaReserva.addItems(sala)

        
    

        
    def validandoDados(self):
        self.feedbackReserva.setText('Reserva realizada.')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.feedbackReserva))

    def dadosInvalidos(self):
        self.feedbackReserva.setText('Dados incomoletos.')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.feedbackReserva))

    def limparCampos(self, campo):
        campo.clear()