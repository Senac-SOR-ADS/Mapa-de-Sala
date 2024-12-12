from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QPoint

class FeadbackConcluido(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/feadbackConcluido.ui', self)
        
        # Variáveis para armazenar o estado da movimentação
        self._is_dragging = False
        self._start_pos = QPoint()

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
