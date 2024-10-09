from view.cadastrarSalas import CadastrarSalas
from model.sala import Sala

class SalaController(CadastrarSalas):
    def __init__(self):
        super().__init__()
        self.show()

        self.cadastrarSala.clicked.connect(self.cadastroDeSala)

    def validarCampos(self) -> bool:
        if not self.nomeSala.text().strip():
            return False
        
        elif not self.tipoEquipamento.text().strip():
            return False
        
        elif not self.mediaCapacidade.text().strip():
            return False
        
        else:
            return True

    def cadastroDeSala(self):
        nomeRetornado, tipoRetornado, predioRetornado, equipamentoRetornado, capacidadeRetornada, feedbackRetornado = self.getCadastroSalas()
        sala = Sala(nomeRetornado, tipoRetornado, predioRetornado, equipamentoRetornado, capacidadeRetornada, feedbackRetornado)
        if self.validarCampos():
            sala.cadastrar_sala()
        else:
            print('Porfavor, preencha os campos necessários')