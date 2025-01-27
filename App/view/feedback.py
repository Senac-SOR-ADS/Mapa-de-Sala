from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap
from PyQt5 import QtMultimedia
from PyQt5 import QtCore
import os
from winotify import Notification, audio


class Feedback(QDialog):
    def __init__(self, type, txt, icon, aviso, typemsg):
        super().__init__()
        loadUi('App/view/ui/feedback.ui', self)
        
        # Variáveis para armazenar o estado da movimentação
        self._is_dragging = False
        self._start_pos = QPoint()
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.btnFechar.clicked.connect(self.accept)
        
        self.texto.setText(txt)
        
        self.icon.setPixmap(QPixmap(icon))   
        self.player = QtMultimedia.QMediaPlayer()
        
        #notificação de erro
        if type == False:
            # toca alertinha de erro
            CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
            filename = os.path.join(CURRENT_DIR, "./ui/musicas/erroToque.mp3")
            url = QtCore.QUrl.fromLocalFile(filename)
            self.player.setMedia(QtMultimedia.QMediaContent(url))
            self.player.play()
            
            #mostra uma notificação no windows para o usuario sobre o erro
            notificacao = Notification( app_id='Mapa de Sala',
                                       title=aviso,
                                       msg=typemsg, 
                                       icon=r'C://xampp/htdocs/interfaceS/App/view/ui/icones/iconNotificacao.png' )
            # notificacao.set_audio(audio.LoopingCall2, loop=False)
            notificacao.add_actions(label='Fechar')
            notificacao.show()
            
        #notificação de sucesso
        if type == True:
            # toca alertinha de erro
            CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
            filename = os.path.join(CURRENT_DIR, "./ui/musicas/sucessoNotificacao.mp3")
            url = QtCore.QUrl.fromLocalFile(filename)
            self.player.setMedia(QtMultimedia.QMediaContent(url))
            self.player.play()
            
            #mostra uma notificação no windows para o usuario sobre o erro
            notificacao = Notification( app_id='Mapa de Sala',
                                       title=aviso,
                                       msg=typemsg,
                                       icon=r'C://xampp/htdocs/interfaceS/App/view/ui/icones/iconNotificacao.png' )
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
            
    # def tocarErro(self):
    #     CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    #     filename = os.path.join(CURRENT_DIR, "./ui/musicaTeste/error-2-126514.mp3")
    #     url = QtCore.QUrl.fromLocalFile(filename)
    #     self.player.setMedia(QtMultimedia.QMediaContent(url))
    #     self.player.play()

# if __name__ == "__main__":
#     from PyQt5.QtWidgets import QApplication
#     app = QApplication([])
#     if Feedback('teste').exec_():
#         print('ok')
#     else:
#         print('negado')