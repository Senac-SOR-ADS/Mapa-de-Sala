from view.cadastrarSalas import CadastrarSalas
from model.sala import Sala

class SalaController(CadastrarSalas):
    def __init__(self):
        super().__init__()
        self.show()

        self.cadastrarSala.clicked.connect(self.cadastroDeSala)

    def validarCampos(self):
        if not self.nomeSala.text().strip():
            print('Falta o nome da sala')
            return False
        if not self.tipoSala.currentText().strip():
            print('Falta o tipo da sala')
            return False

    def cadastroDeSala(self):
        nomeRetornado, tipoRetornado, predioRetornado, equipamentoRetornado, capacidadeRetornada, feedbackRetornado = self.getCadastroSalas()
        sala = Sala(nomeRetornado, tipoRetornado, predioRetornado, equipamentoRetornado, capacidadeRetornada, feedbackRetornado)
        sala.cadastrar_sala()