from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from .cadastroPessoas import cadastroPessoas
from .reserva import ReservaInterface
from .cadastrarArea import CadastrarArea
from .cadastrarCurso import CadastrarCurso


class HomePrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/interfaceHomeV1.ui',self)

   # Criando instancias das interfaces
        self.interfCasPessoa = cadastroPessoas()
        self.interfReserva = ReservaInterface()
        self.interfCasArea = CadastrarArea()
        self.interfCasCurso = CadastrarCurso()
        self.inserirTelas( [self.interfCasPessoa, self.interfReserva, self.interfCasArea, self.interfCasCurso] )

        self.btnCadastrarPessoa.clicked.connect(lambda: self.trocarTela(self.interfCasPessoa))
        self.btnReserva.clicked.connect(lambda: self.trocarTela(self.interfReserva))
        self.btnIncio.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.inicio))
        self.btnArea.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.interfCasArea))
        self.btnCurso.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.interfCasCurso))

    def inserirTelas(self, telas):
        for interface in telas:
            self.stackedWidget.addWidget(interface)

    def trocarTela(self, tela):
        """Função para trocar as tela. Necessario
        passar a classe da tela"""
        self.stackedWidget.setCurrentWidget(tela)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moving = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.moving:
            self.move(self.pos() + event.pos() - self.offset)

    def mouseReleaseEvent(self, event):
        self.moving = False
        
if __name__ == "__main__":
    app = QApplication([])
    widget = HomePrincipal()
    widget.show()
    app.exec_()
 