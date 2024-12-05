from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt


class TelaConfirmacao(QDialog):
    def __init__(self, aviso):
        super().__init__()
        loadUi('App/view/ui/telaConfirmacao.ui', self)
        self.aviso.setText(aviso)
        self.btnOk.clicked.connect(self.accept)
        self.btnCancelar.clicked.connect(self.reject)
        self.btnFechar.clicked.connect(self.reject)
        
        # Remove a barra de título e as bordas da janela
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        
    # def mouseMoveEvent(self, event):
    #     if self.moving and not self.isMaximized():
    #         self.move(self.pos() + event.pos() - self.offset)
        
        
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    info = TelaConfirmacao('Teste')
    if info.exec_():
        print('ok')
    else:
        print('negado')
    
