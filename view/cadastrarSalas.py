from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt

class CadastrarSalas(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('view/ui/cadastroSalas.ui',self)

    def getCadastroSalas(self):
        nome = self.nomeSala.text().strip()
        sala = self.tipoSala.currentText().strip()
        predio = self.nomePredio.currentText().strip()
        equipamento = self.tipoEquipamento.text().strip()
        capacidade = self.mediaCapacidade.text().strip()
        feedback = self.feedbackText.text().strip()

        return(nome, sala, predio, equipamento, capacidade, feedback)



    
