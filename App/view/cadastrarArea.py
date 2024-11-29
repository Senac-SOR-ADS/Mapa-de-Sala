from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer, pyqtSlot
from App.controller.area import cadastroDeArea
from App.controller.utils import validarAcao
from App.controller.utils import validarInputs


class CadastrarArea(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/cadastroArea.ui',self)

    @pyqtSlot()
    def on_btnCadastrarArea_clicked(self):
        nomeArea = self.getCadastroArea()
        if validarInputs([nomeArea]):
            cadastroDeArea(nomeArea)
            validarAcao()
        validarAcao(False)
        
    def getCadastroArea(self):
        area = self.cadastrarArea.text().strip()
        return(area)

    def validandoDados(self):
        self.resposta.setText('CADASTRANDO...')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.resposta))

    def dadosInvalidos(self):
        texto = 'DADOS INCOMPLETOS.'
        self.resposta.setText(texto)
        QTimer.singleShot(2000, lambda: self.limparCampos(self.resposta))

    def limparCampos(self, campo):
        campo.clear()
