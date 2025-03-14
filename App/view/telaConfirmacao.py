from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QPoint
from .telaConflitos import TelaConflitos


class TelaConfirmacao(QDialog):
    def __init__(self, titulo, aviso, txtBtnOk, btnConflitos=False, equipamentos=False):
        super().__init__()
        loadUi('App/view/ui/telaConfirmacao.ui', self)
        self._is_dragging = False
        self._start_pos = QPoint()
        
        self.checkBoxEquipamentos.setStyleSheet("""
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
        
        if btnConflitos == False:
            self.btnAbrirConflitos.hide()
        else: 
            self.btnAbrirConflitos.show()
        
        if aviso == '':
            self.aviso.close()
        else:
            self.aviso.setText(aviso)
            
            
        self.titulo.setText(titulo)
        self.btnOk.clicked.connect(self.accept)
        self.btnCancelar.clicked.connect(self.reject)
        self.btnFechar.clicked.connect(self.reject)
        self.btnAbrirConflitos.clicked.connect(self.chamarTelaConflitos)
        
        # Remove a barra de título e as bordas da janela
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.btnOk.setText(txtBtnOk)

        if equipamentos == True:
            self.containerEquipamentos.show()
        else:
            self.containerEquipamentos.hide()
            
            
    def chamarTelaConflitos(self):
        conflitos = TelaConflitos('')
        if conflitos.exec_():
            pass

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._is_dragging = True
            self._start_pos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self._is_dragging and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self._start_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._is_dragging = False
            event.accept()
        
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    info = TelaConfirmacao('txt', 'Teste', "Sim")
    if info.exec_():
        print('ok')
    else:
        print('negado')
    
