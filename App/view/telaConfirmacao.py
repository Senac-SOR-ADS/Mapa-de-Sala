from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt


class TelaConfirmacao(QDialog):
    def __init__(self, titulo, aviso, txtBtnOk, equipamentos=False):
        super().__init__()
        loadUi('App/view/ui/telaConfirmacao.ui', self)
        
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
        
        if aviso == '':
            self.aviso.close()
        else:
            self.aviso.setText(aviso)
        self.titulo.setText(titulo)
        self.btnOk.clicked.connect(self.accept)
        self.btnCancelar.clicked.connect(self.reject)
        self.btnFechar.clicked.connect(self.reject)
        
        # Remove a barra de título e as bordas da janela
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.btnOk.setText(txtBtnOk)

        if equipamentos == True:
            self.containerEquipamentos.show()
        else:
            self.containerEquipamentos.hide()
        
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    info = TelaConfirmacao('txt', 'Teste', "Sim")
    if info.exec_():
        print('ok')
    else:
        print('negado')
    
