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

    def __init__(self, type, txt, aviso, typemsg):
        super().__init__()
        loadUi('App/view/ui/feedback.ui', self)
        # Variáveis para armazenar o estado da movimentação
        self._is_dragging = False
        self._start_pos = QPoint()
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.btnFechar2.clicked.connect(self.reject)
        self.btnFechar.clicked.connect(self.accept)
        
        self.texto.setText(txt)
        

        self.player = QtMultimedia.QMediaPlayer()

        
        #notificação de erro
        if type == False:
            icon_path = os.path.join(self.CURRENT_DIR, r"./ui/icones/iconErro.png")
            self.icon.setPixmap(QPixmap(icon_path))
            # toca alertinha de erro
            filename = os.path.join(self.CURRENT_DIR, "./ui/sounds/erroToque.mp3")
            url = QtCore.QUrl.fromLocalFile(filename)
            self.player.setMedia(QtMultimedia.QMediaContent(url))
            self.player.play()
            
            #mostra uma notificação no windows para o usuario sobre o erro
            filenameNotificacao = os.path.join(self.CURRENT_DIR, r"ui\icones\iconNotificacao.png")
            notificacao = Notification( app_id='Mapa de Sala',
                                       title=aviso,
                                       msg=typemsg, 
                                       icon=filenameNotificacao )
            # notificacao.set_audio(audio.LoopingCall2, loop=False)
            notificacao.add_actions(label='Fechar')
            notificacao.show()
            
        #notificação de sucesso
        if type == True:
            icon_path = os.path.join(self.CURRENT_DIR, r"./ui/icones/iconConcluido.png")
            self.icon.setPixmap(QPixmap(icon_path))
            # toca alertinha de erro
            filename = os.path.join(self.CURRENT_DIR, "./ui/sounds/sucessoNotificacao.mp3")
            url = QtCore.QUrl.fromLocalFile(filename)
            self.player.setMedia(QtMultimedia.QMediaContent(url))
            self.player.play()
            
            #mostra uma notificação no windows para o usuario sobre o erro
            notificacao = Notification( app_id='Mapa de Sala',
                                       title=aviso,
                                       msg=typemsg,
                                       icon=filenameNotificacao )
            # notificacao.set_audio(audio.LoopingCall2, loop=False)
            notificacao.add_actions(label='Fechar')
            notificacao.show()

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
