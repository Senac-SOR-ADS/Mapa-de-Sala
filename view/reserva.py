from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QTimer, pyqtSlot



class ReservaInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('view/ui/reserva.ui',self)

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
        """Função para realizar os tratamentos dos dados após o click 
        no botão btnFazerReserva(Reserva)"""
        return self.getDados()
        
    def validandoDados(self):
        self.feedbackReserva.setText('Reserva realizada.')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.feedbackReserva))

    def dadosInvalidos(self):
        self.feedbackReserva.setText('Dados incomoletos.')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.feedbackReserva))

    def limparCampos(self, campo):
        campo.clear()

if __name__ == "__main__":
    app = QApplication([])
    widget = ReservaInterface()
    widget.show()
    app.exec_()


