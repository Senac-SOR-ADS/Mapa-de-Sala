from view.cadastrarSalas import CadastrarSalas
from model.sala import Sala

class SalaController(CadastrarSalas):
    def __init__(self):
        super().__init__()
        self.show()

        self.cadastrarSala.clicked.connect(self.cadastroDeSala)

    def cadastroDeSala(self):
        for i in self.getCadastroSalas():
            if not i:
                print('não vai cadastrar')
                return False
            else:
                pass
        # nomeRetornado, tipoRetornado, predioRetornado, equipamentoRetornado, capacidadeRetornada, feedbackRetornado = self.getCadastroSalas()
        # sala = Sala(nomeRetornado, tipoRetornado, predioRetornado, equipamentoRetornado, capacidadeRetornada, feedbackRetornado)
        # sala.cadastrar_sala()