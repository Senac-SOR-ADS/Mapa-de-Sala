from PyQt5.QtWidgets import QWidget, QDateEdit
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer, QDate, pyqtSlot

# from App.model.reserva import Reserva
# from App.model.login import Login
# Não está sendo utilizado no arquivo

from App.controller.curso import listarCursos
from App.controller.pessoa import buscarPessoas
from App.controller.sala import listarSala
from App.controller.utils import modificarData
from App.controller.reserva import fazendoReserva, validarCadastro


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
        self.diaInicio.dateChanged.connect(self.setDataMinima)

        self.diaFim.setCalendarPopup(True)
        self.diaFim.setDisplayFormat('dd/MM/yyyy')
        self.diaFim.setDate(QDate.currentDate()) 

    def getDados(self)->dict:
        """Pegando o dados na interface e retornando os valores"""
        pessoas = buscarPessoas()
        sala = listarSala()
        curso = listarCursos() 
        nomeDocenteResponsavel = self.nomeDocente.currentText().strip()
        idDocente = pessoas[nomeDocenteResponsavel]
        nomeSala = self.salaReserva.currentText().strip()
        idSala = sala[nomeSala]
        nomeCurso = self.cursoReserva.currentText().strip()
        idCurso = curso[nomeCurso]
        
        
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
        validacao = validarCadastro(info, diasValidos)
        if type(validacao) == list:
            print('Não foi possível fazer a reserva, já existe uma reserva nesse horário')
        elif not validacao:
            fazendoReserva(idLogin, info, diasValidos)
    
    
    def setDataMinima(self):
        primeiroDia = self.diaInicio.date()
        self.diaFim.setMinimumDate(primeiroDia)
    
        
    def popularJanela(self):
        """Popula os comboBoxes com dados do banco."""
        self.comboBoxCurso()
        self.comboBoxPessoa()
        self.comboBoxSala()

    def comboBoxCurso(self):
        cursos = listarCursos()
        self.cursoReserva.clear()
        self.cursoReserva.addItems(cursos.keys())

    def comboBoxPessoa(self):
        """Busca as pessoas no banco e popula o comboBox."""
        pessoas = buscarPessoas()
        self.nomeDocente.clear()
        self.nomeDocente.addItems(pessoas.keys())

    def comboBoxSala(self):
        """Busca as salas no banco e popula o comboBox."""
        salas = listarSala()
        self.salaReserva.clear()
        self.salaReserva.addItems(salas.keys())

    def validandoDados(self):
        self.feedbackReserva.setText('Reserva realizada.')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.feedbackReserva))

    def dadosInvalidos(self):
        self.feedbackReserva.setText('Dados incomoletos.')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.feedbackReserva))

    def limparCampos(self, campo):
        campo.clear()