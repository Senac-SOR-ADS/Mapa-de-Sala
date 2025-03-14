from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap
from PyQt5 import QtMultimedia
from PyQt5 import QtCore
import os
from winotify import Notification, audio



class Feedback(QDialog):
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


    def __init__(self, tipo:bool, txt:str, aviso:str, typemsg:str):
        super().__init__()
        loadUi('App/view/ui/feedback.ui', self)
        # Variáveis para armazenar o estado da movimentação
        self._is_dragging = False
        self._start_pos = QPoint()
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.btnFechar2.clicked.connect(self.reject)
        self.btnFechar.clicked.connect(self.accept)
        self.texto.setText(txt)
        self.player = QtMultimedia.QMediaPlayer()
        self.notificacao(aviso, typemsg)
        self.tocarAudio(tipo)
        
        # notificação de sucesso
        icon_path = os.path.join(self.CURRENT_DIR, r"./ui/icones/iconConcluido.png")
        if tipo == False:
            icon_path = os.path.join(self.CURRENT_DIR, r"./ui/icones/iconErro2.png")
        self.icon.setPixmap(QPixmap(icon_path))
        


    def notificacao(self, aviso, typemsg):
        filenameNotificacao = os.path.join(self.CURRENT_DIR, r"ui\icones\iconNotificacao.png")
        notificacao = Notification(app_id='Mapa de Sala', title=aviso, msg=typemsg, icon=filenameNotificacao)
        notificacao.add_actions(label='Fechar')
        notificacao.show()

    def tocarAudio(self, sucesso=True):
        som = 'sucessoNotificacao' if sucesso else 'erroToque'
        url = QtCore.QUrl.fromLocalFile(os.path.join(self.CURRENT_DIR, f"./ui/sounds/{som}.mp3"))
        self.player.setMedia(QtMultimedia.QMediaContent(url))
        self.player.play()

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
