from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QTimer, pyqtSlot

class CadastrarCurso(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('view/ui/cadastroCurso.ui',self)

    def getCadastroCurso(self):
        nome = self.nomeCurso.text().strip()
        periodo = self.periodoCurso.text().strip()
        horas = self.horasPorDia.text().strip()
        oferta = self.ofertaCurso.text().strip()
        carga = self.cargaCurso.text().strip()
        alunos = self.quantidadeAlunos.text().strip()
        
        return(nome, periodo, horas, oferta, carga, alunos)

    def validandoDados(self):
        self.respostaCadastrando.setText('CADASTRANDO...')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.respostaCadastrando))

    def dadosInvalidos(self):
        texto = 'DADOS INCOMPLETOS.'
        self.respostaCadastroIncompleto.setText(texto)
        QTimer.singleShot(2000, lambda: self.limparCampos(self.respostaCadastroIncompleto))

    def limparCampos(self, campo):
        campo.clear()

