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
        self.temaController.temaMudado.connect(self.funcaoTemaGlobal)


        self.temas = [
            'App/view/ui/css/temaClaro/temaPrincipal.css',
            'App/view/ui/css/temaEscuro/temaPrincipal.css'
        ]
        self.temaAtual = 0

        # Configura o estado inicial do checkbox
        self.btnMudarTema.setChecked(self.temaAtual == 1)
        self.atualizarTema()

        # Conecta o estado do checkbox à função de mudar tema
        self.btnMudarTema.stateChanged.connect(self.mudarTema)
    
        
    def funcaoTemaGlobal(self, tema):
        try:
            with open(tema, 'r') as f:
                cssTema = f.read()
            # print(f'Conteúdo do CSS:\n{cssTema}')   
            QApplication.instance().setStyleSheet(cssTema)
            print(f'Tema aplicado')
        except Exception as e:
            print(f'Erro ao aplicar tema: {e}')


    def mudarTema(self):
        #Atualiza o tema baseado no estado do checkbox
        if self.btnMudarTema.isChecked():
            self.temaAtual = 1  # Tema escuro
        else:
            self.temaAtual = 0
        
        tema = self.temas[self.temaAtual]
        self.temaController.temaMudado.emit(tema)

    def atualizarTema(self):
        tema = self.temas[self.temaAtual]
        self.temaController.temaMudado.emit(tema)
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = ConfigurarTela()
    widget.show()
    sys.exit(app.exec_())
