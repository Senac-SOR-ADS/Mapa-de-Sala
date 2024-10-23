from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.uic import loadUi

class TemaController(QObject):
    temaMudado = pyqtSignal(str)

class ConfigurarTela(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/telaConfiguracoes.ui', self)
        
        self.btnMudarTema.clicked.connect(self.mudarTema)
        # Instância do controlador dos temas
        self.temaController = TemaController()
        self.temaController.temaMudado.connect(self.funcaoTemaGlobal)



        self.temas = [
            'App/view/ui/css/temaClaro/temaPrincipal.css',
            'App/view/ui/css/temaEscuro/temaPrincipal.css'
        ]
        self.temaAtual = 0
    
        
    def funcaoTemaGlobal(self, tema):
        with open(tema, 'r') as f:
            cssTema = f.read()
        QApplication.instance().setStyleSheet(cssTema)


    def mudarTema(self):
        tema = self.temas[self.temaAtual]
        self.temaAtual = (self.temaAtual + 1) % len(self.temas) 
        self.temaController.temaMudado.emit(tema)

    def atualizarTema(self, tema):
        with open(tema, 'r') as f:
            self.setStyleSheet(f.read())
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = ConfigurarTela()
    widget.show()
    sys.exit(app.exec_())
