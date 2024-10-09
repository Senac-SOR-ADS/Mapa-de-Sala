from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from App.controller.sala import cadastrarSala


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
    
    def validarInputs(self):
        campos = self.getCadastroSalas()
        for i in campos:
            if not i:
                return False
        return True
    
    def iniciandoCadastro(self):
        if self.validarInputs():
            nome, sala, predio, equipamento, capacidade, feedback = self.getCadastroSalas()
            cadastrarSala(nome, sala, predio, equipamento, capacidade, feedback)