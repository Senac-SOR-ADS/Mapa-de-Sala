from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSignal, QObject, QTimer
from PyQt5.uic import loadUi

class TemaController(QObject):
    temaMudado = pyqtSignal(str)

class ConfigurarTela(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/telaConfiguracoes.ui', self)
        
        self.btnMudarTema.stateChanged.connect(self.mudarTema)
        # Instância do controlador dos temas
        self.temaController = TemaController()
        self.temaController.temaMudado.connect(self.funcaoTemaGlobal)

        # Faz a exibição dos icones
        self.btnMudarTema.setStyleSheet("""
            QCheckBox::indicator {
                width: 30px;
                height: 30px;
            }
            QCheckBox::indicator:unchecked {
                image: url("App/view/ui/icones/toggleOff.png");
            }
            QCheckBox::indicator:checked {
                image: url("App/view/ui/icones/toggleOn.png");
            }
        """)

        self.temas = [
            'App/view/ui/css/temaEscuro/temaPrincipal.css',
            'App/view/ui/css/temaClaro/temaPrincipal.css'
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

        self.atualizarMensagem()

    def atualizarMensagem(self):
        if self.temaAtual == 0: 
            self.temaEscuro.setVisible(True)   
            self.temaClaro.setVisible(False)  
            self.mensagemTemaEscuro()
        else:  
            self.temaEscuro.setVisible(False)   
            self.temaClaro.setVisible(True) 
            self.mensagemTemaClaro()

    def mensagemTemaClaro(self):
        self.temaClaro.setText('Modo escuro')

    def mensagemTemaEscuro(self):
        self.temaEscuro.setText('Modo claro')

    def atualizarTema(self, tema):
        with open(tema, 'r') as f:
            self.setStyleSheet(f.read())

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = ConfigurarTela()
    widget.show()
    sys.exit(app.exec_())
