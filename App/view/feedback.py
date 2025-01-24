from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QPoint

class Feedback(QDialog):
    def __init__(self, txt):
        super().__init__()
        loadUi('App/view/ui/feedback.ui', self)
        
        # Variáveis para armazenar o estado da movimentação
        self._is_dragging = False
        self._start_pos = QPoint()
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.btnFechar.clicked.connect(self.accept)
        
        self.texto.setText(txt)

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
    if Feedback('teste').exec_():
        print('ok')
    else:
        print('negado')