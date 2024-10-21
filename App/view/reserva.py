from PyQt5.QtWidgets import QWidget, QDateEdit
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer, QDate, pyqtSlot
from App.model.reserva import Reserva

from App.controller.curso import listarCursos
from App.controller.pessoa import buscaPessoas
from App.controller.sala import listarSala
from App.controller.reserva import validarDia

from App.model.login import Login

class ReservaInterface(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/reserva.ui',self)
        self.popularJanela()

        # Os metodos abaixo servem para transformar o QDateEdit em um calendário
        self.diaInicio = self.findChild(QDateEdit, 'diaInicio') 
        self.diaFim = self.findChild(QDateEdit, 'diaFim')  

        self.diaInicio.setCalendarPopup(True)
        self.diaInicio.setDisplayFormat('dd/MM/yyyy')
        self.diaInicio.setDate(QDate.currentDate())  

        self.diaFim.setCalendarPopup(True)
        self.diaFim.setDisplayFormat('dd/MM/yyyy')
        self.diaFim.setDate(QDate.currentDate()) 

    def getDados(self)->dict:
        """Pegando o dados na interface e retornando os valores"""
        nomeDocenteResponsavel = self.nomeDocente.currentText().strip() 
        nomeSala = self.salaReserva.currentText().strip() 
        nomeCurso = self.cursoReserva.currentText().strip() 
        equipamentos = self.equipamentosReserva.text().strip() 
        inicio = self.diaInicio.text().strip() 
        fim = self.diaFim.text().strip() 
        observacao = self.observacaoReserva.text().strip() 
        cursoInicio = self.inicioCurso.time().toString('HH:mm')
        cursoFim = self.fimCurso.time().toString('HH:mm')
        segunda = self.segCheck.isChecked()        
        terca = self.terCheck.isChecked()
        quarta = self.quaCheck.isChecked()
        quinta = self.quiCheck.isChecked()
        sexta = self.sextaCheck.isChecked()
        sabado = self.sabCheck.isChecked()

        dados = {"nomeDocente":nomeDocenteResponsavel, 
                 "nomeSala":nomeSala, 
                 "nomeCurso":nomeCurso,
                 "equipamentos":equipamentos,
                 "inicio":inicio,
                 "fim":fim,
                 "observações":observacao,
                 "inicioCurso":cursoInicio,
                 "fimCurso":cursoFim,
                 "seg":segunda,
                 "ter":terca,
                 "qua":quarta,
                 "qui":quinta,
                 "sexta":sexta,
                 "sab":sabado}
        return dados
    
    @pyqtSlot()
    def on_btnFazerReserva_clicked(self):
        # info = self.getDados()
        # idLogin = Login.getIdLogin()
        # if Reserva(idLogin, info).fazer_reserva():
        #     print('ok')       
        DataInicio = self.getDados()
        DataFim =  self.getDados()
        DataInicio = DataInicio["inicio"]
        DataFim = DataFim["fim"]
        validarDia(DataInicio, DataFim)
            

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

    def testeDias(self):
        diaInicio = self.getDados().values()
        print(diaInicio)
        validarDia()
        
    

        
    def validandoDados(self):
        self.feedbackReserva.setText('Reserva realizada.')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.feedbackReserva))

    def dadosInvalidos(self):
        self.feedbackReserva.setText('Dados incomoletos.')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.feedbackReserva))

    def limparCampos(self, campo):
        campo.clear()