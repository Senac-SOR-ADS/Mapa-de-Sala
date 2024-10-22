from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.uic import loadUi

class TemaController(QObject):
    temaMudado = pyqtSignal(str)

class ConfigurarTela(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/telaConfiguracoes.ui', self)
        
        # Instância do controlador dos temas
        self.temaController = TemaController()
        self.temaController.temaMudado.connect(self.atualizarTema)

        self.temaAtual = 0
        self.temas = [
            "background-color: white; color: black;",
            "background-color: black; color: white;",
            "background-color: #282C34; color: #61AFEF;",
        ]

        # Conecta à função de mudarTema
        self.btnMudarTema.clicked.connect(self.mudarTema)

    def mudarTema(self):
        tema = self.temas[self.temaAtual]
        self.temaAtual = (self.temaAtual + 1) % len(self.temas) # Atualiza o próximo tema
        self.temaController.temaMudado.emit(tema) # Emite o sinal sobre as trocas de temas

    def atualizarTema(self, tema):
        QApplication.instance().setStyleSheet(f"QWidget {{ {tema} }}")  

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = ConfigurarTela()
    widget.show()
    sys.exit(app.exec_())
