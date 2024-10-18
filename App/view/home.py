from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, pyqtSlot
from .cadastroPessoas import cadastroPessoas
from .reserva import ReservaInterface
from .cadastrarArea import CadastrarArea
from .cadastrarCurso import CadastrarCurso
from .cadastrarLogin import CadastroLogin


class HomePrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/home.ui',self)
        self.moving = False
        self.subMenuLateral.hide()
        
   # Criando parte interativa do menu
   
        self.btnMenu: QPushButton
        self.subMenuLateral: QWidget

   # Criando instancias das interfaces
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.interfCasPessoa = cadastroPessoas()
        self.interfReserva = ReservaInterface()
        self.interfCasArea = CadastrarArea()
        self.interfCasCurso = CadastrarCurso()
        self.interfCasLogin = CadastroLogin()
        self.inserirTelas( [self.interfCasPessoa, self.interfReserva, self.interfCasArea, self.interfCasCurso, self.interfCasLogin] )

        self.btnCadastrarPessoa.clicked.connect(lambda: self.trocarTela(self.interfCasPessoa))
        self.btnReserva.clicked.connect(lambda: self.trocarTela(self.interfReserva))
        self.btnIncio.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.inicio))
        self.btnArea.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.interfCasArea))
        self.btnCurso.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.interfCasCurso))
        self.btnCadastroLogin.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.interfCasLogin))
        self.btnMinimizar.clicked.connect(self.showMinimized)
        self.btnFecharPagina.clicked.connect(self.close)
        self.btnTelaCheia.clicked.connect(self.windowConnect)

    # Faz o botão de Tela Cheia ao ser executado, retornar ao normal
    def windowConnect(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def inserirTelas(self, telas):
        for interface in telas:
            self.stackedWidget.addWidget(interface)

    def trocarTela(self, tela):
        """Função para trocar as tela. Necessario
        passar a classe da tela"""
        self.stackedWidget.setCurrentWidget(tela)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            return
        if event.button() == Qt.LeftButton:
            self.moving = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.moving:
            self.move(self.pos() + event.pos() - self.offset)

    def mouseReleaseEvent(self, event):
        self.moving = False
    
    @pyqtSlot()
    def on_btnMenu_clicked(self):
        if (self.subMenuLateral.isVisible()):
            self.subMenuLateral.hide()
        else:
            self.subMenuLateral.show()

        
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    widget = HomePrincipal()
    widget.show()
    app.exec_()
 