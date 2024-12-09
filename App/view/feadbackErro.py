from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QPoint

class FeadbackErro(QDialog):
    def __init__(self, txt):
        super().__init__()
        loadUi('App/view/ui/feadbackErro.ui', self)
        
        self.texto.setText(txt)
        
        # Remove a barra de título e as bordas da janela
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        # Variáveis para controle de movimentação
        self._is_dragging = False
        self._start_pos = QPoint()
        
        # Botões
        self.btnConfirmar.clicked.connect(self.reject)
        self.btnFechar.clicked.connect(self.reject)

    def mudarFoto(self, img):
        if img == 'Validado':
            self.setStyleSheet("""
                                #icon {
                                    image: url(App/view/ui/icones/iconConcluido.png);
                                }
                                """)
        else:
            self.setStyleSheet("""
                                #icon {
                                    image: url(App/view/ui/icones/iconErro.png);
                                }
                                """)

    # Adiciona movimentação da janela
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
    resp = FeadbackErro('Texto de exemplo')
    app = QApplication([])
    if resp.exec_():
        print('ok')
    else:
        print('negado')
