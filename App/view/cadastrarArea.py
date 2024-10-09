from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer

class CadastrarArea(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/cadastroArea.ui',self)

    def getCadastroArea(self):
        area = self.cadastrarArea.text().strip()

        return(area)


    def validandoDados(self):
        self.respostaCadastrando.setText('CADASTRANDO...')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.respostaCadastrando))

    def dadosInvalidos(self):
        texto = 'DADOS INCOMPLETOS.'
        self.respostaNaoCadastrado.setText(texto)
        QTimer.singleShot(2000, lambda: self.limparCampos(self.respostaNaoCadastrado))

    def limparCampos(self, campo):
        campo.clear()




