from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer



class ReservaInterface(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/reserva.ui',self)

    def getDados(self)->dict:
        """Pegando o dados na interface e retornando os valores"""
        nomeDocenteResponsavel = self.nomeDocente.currentText().strip() 
        nomeSala = self.salaReserva.currentText().strip() 
        nomeCurso = self.cursoReserva.currentText().strip() 
        equipamentos = self.equipamentosReserva.text().strip() 
        inicio = self.diaInicio.text().strip() 
        fim = self.diaFim.text().strip() 
        observacao = self.observacaoReserva.text().strip() 
        cursoInicio = self.inicioCurso.currentTime().strip()
        cursoFim = self.fimCurso.currentTime().strip()
        segunda = self.segCheck.ch_check().strip()        
        terca = self.terCheck.ch_check().strip()
        quarta = self.quaCheck.ch_check().strip()
        quinta = self.quiCheck.ch_check().strip()
        sexta = self.sextaCheck.ch_check().strip()
        sabado = self.sabCheck.ch_check().strip()

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
        
    def validandoDados(self):
        self.feedbackReserva.setText('Reserva realizada.')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.feedbackReserva))

    def dadosInvalidos(self):
        self.feedbackReserva.setText('Dados incomoletos.')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.feedbackReserva))

    def limparCampos(self, campo):
        campo.clear()


