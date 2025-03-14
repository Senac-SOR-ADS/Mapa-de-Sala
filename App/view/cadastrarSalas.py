from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from App.controller.sala import cadastrarSala
from App.controller.utils import validarInputs, sucessoCadastro, erroCadastro


class CadastrarSalas(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/cadastroSalas.ui',self)

        self.cadastrarSala.clicked.connect(self.iniciandoCadastro)

    def getCadastroSalas(self):
        nome = self.nomeSala.text().strip()
        sala = self.tipoSala.currentText().strip()
        predio = self.nomePredio.currentText().strip()
        equipamento = self.tipoEquipamento.text().strip()
        capacidade = self.mediaCapacidade.text().strip()
        feedback = self.feedbackText.text().strip()

        return (nome, sala, predio, equipamento, capacidade, feedback)
    
    def iniciandoCadastro(self):
        valores = self.getCadastroSalas()
        if not validarInputs(valores[:-1]):
            erroCadastro(self)
        else:
            if cadastrarSala(valores[0], valores[1], valores[2], valores[3], valores[4], valores[5]):
                sucessoCadastro(self)   
                self.limparCampos()
    

    def limparCampos(self):
        self.nomeSala.clear()
        self.tipoSala.setCurrentIndex(0)
        self.nomePredio.setCurrentIndex(0)
        self.tipoEquipamento.clear()
        self.mediaCapacidade.setValue(1)
        self.feedbackText.clear()
 