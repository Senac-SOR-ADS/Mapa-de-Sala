from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt

class FeadbackErro(QDialog):
    def __init__(self, txt):
        super().__init__()
        loadUi('App/view/ui/feadbackErro.ui',self)
        
        self.texto.setText(txt)
        # self.setStyleSheet(icon)
        
        self.btnConfirmar.clicked.connect(self.reject)
        
        # Remove a barra de título e as bordas da janela
        self.setWindowFlags(Qt.FramelessWindowHint)
    
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    resp = FeadbackErro('sla')
    app = QApplication([])
    if resp.show():
        print('ok')
    else:
        print('negado')