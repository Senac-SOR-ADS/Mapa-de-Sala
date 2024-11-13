from PyQt5.QtWidgets import QWidget, QDateEdit
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer, QDate, pyqtSlot
from App.model.reserva import Reserva


from App.controller.curso import listarCursos
from App.controller.pessoa import buscarPessoas
from App.controller.utils import modificarData
from App.controller.sala import listarSala
from App.controller.reserva import fazendoReserva, validarCadastro

from App.model.login import Login

class ReservaInterface(QWidget):
    curso = listarCursos()
    pessoa = buscarPessoas()
    sala = listarSala()
    
    
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
        idDocente = self.pessoa[nomeDocenteResponsavel]
        nomeSala = self.salaReserva.currentText().strip()
        idSala = self.sala[nomeSala]
        nomeCurso = self.cursoReserva.currentText().strip()
        idCurso = self.curso[nomeCurso]
        
        equipamentos = self.equipamentosReserva.text().strip() 
        diaInicio = modificarData(self.diaInicio.text().strip() )
        diaFim = modificarData(self.diaFim.text().strip() )
        observacao = self.observacaoReserva.text().strip() 
        cursoInicio = self.inicioCurso.time().toString('HH:mm')
        cursoFim = self.fimCurso.time().toString('HH:mm')
        segunda = self.segCheck.isChecked()        
        terca = self.terCheck.isChecked()
        quarta = self.quaCheck.isChecked()
        quinta = self.quiCheck.isChecked()
        sexta = self.sextaCheck.isChecked()
        sabado = self.sabCheck.isChecked()

        dados = {"idDocente":idDocente, 
                 "idSala":idSala, 
                 "idCurso":idCurso,
                 "equipamentos":equipamentos,
                 "diaInicio":diaInicio,
                 "diaFim":diaFim,
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
        info = self.getDados()
        idLogin = 8
        diasValidos = (info['seg'], info['ter'], info['qua'], info['qui'], info['sexta'], info['sab'], False)
        if validarCadastro(idLogin, info, diasValidos):
            fazendoReserva(idLogin, info, diasValidos)
        

    def popularJanela(self):
        self.comboBoxCurso()
        self.comboBoxPessoa()
        self.comboBoxSala()

    def comboBoxCurso(self):
        self.cursoReserva.addItems(self.curso.keys())

    def comboBoxPessoa(self):
        self.nomeDocente.addItems(self.pessoa.keys())

    def comboBoxSala(self):
        self.salaReserva.addItems(self.sala.keys())

    def validandoDados(self):
        self.feedbackReserva.setText('Reserva realizada.')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.feedbackReserva))

    def dadosInvalidos(self):
        self.feedbackReserva.setText('Dados incomoletos.')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.feedbackReserva))

    def limparCampos(self, campo):
        campo.clear()