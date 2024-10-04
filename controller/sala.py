from view.cadastrarSalas import CadastrarSalas
from model.sala import Sala

class SalaController(CadastrarSalas):
    def __init__(self):
        super().__init__()
        self.show()

        self.btnCadastrarSala.clicked.connect(self.cadastroDeSala)

    def cadastroDeSala(self):
        nomeRetornado, tipoRetornado, predioRetornado, equipamentoRetornado, capacidadeRetornada = self.getCadastroSalas()
        sala = Sala(nomeRetornado, tipoRetornado, predioRetornado, equipamentoRetornado, capacidadeRetornada, '')