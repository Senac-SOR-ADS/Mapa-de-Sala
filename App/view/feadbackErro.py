from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt

class FeadbackErro(QDialog):
    def __init__(self, txt):
        super().__init__()
        loadUi('App/view/ui/feadbackErro.ui',self)
        
        self.texto.setText(txt)
        
        # Remove a barra de título e as bordas da janela
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.btnConfirmar.clicked.connect(self.reject)
        self.btnFechar.clicked.connect(self.reject)
        
    def mudarFoto(self, img):
        if img == 'Validado':
            self.setStyleSheet("""
                                #icon {
                                    image: url(App/view/ui/icones/iconConcluido.png)
                                }
                                    """)
        else:
            self.setStyleSheet("""
                                #icon {
                                    image: url(App/view/ui/icones/iconErro.png)
                                }
                                    """)
        
        
    
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    resp = FeadbackErro('sla')
    app = QApplication([])
    if resp.exec_():
        print('ok')
    else:
        print('negado')