from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QStackedWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, pyqtSlot, QTimer

# Interfaces
from .cadastroPessoas import cadastroPessoas
from .cadastrarArea import CadastrarArea
from .cadastrarCurso import CadastrarCurso
from .cadastrarLogin import CadastroLogin
from .cadastrarSalas import CadastrarSalas
from .configurarTela import ConfigurarTela
from .editarPessoas import EditarPessoas
from .editarArea import EditarArea
from .editarCurso import EditarCurso
from .editarLogin import EditarLogin
from .editarReserva import EditarReserva
from .editarSala import EditarSala
from .reserva import ReservaInterface
from .telaConfirmacao import TelaConfirmacao

from App.controller.login import pegarUsuarioLogado, removerUsuarioLogado

class HomePrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/home.ui', self)
        self.moving = False
        self.subMenuLateral.hide()
        self.subMenuQuebrado.hide()
        self.btnHome.setChecked(True)
        self._resizing = False
        self._resize_direction = None
        self._resize_timer = QTimer()
        self._resize_timer.setSingleShot(True)
        self._resize_timer.timeout.connect(self._apply_resize)
        self._resize_geometry = None

        # Criando parte interativa do menu
        self.btnMenu: QPushButton
        self.subMenuLateral: QWidget
        self.subMenuQuebrado: QWidget
        self.menuQuebrado: QStackedWidget
        self.cadastros: QWidget
        self.busca: QWidget
        self.editar: QWidget
        self.menuSimples: QWidget
        self.btnHome: QPushButton

        # Criando instâncias das interfaces
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.interfCasPessoa = cadastroPessoas
        self.interfcasSala = CadastrarSalas
        self.interfCasArea = CadastrarArea
        self.interfCasLogin = CadastroLogin
        self.interfCongiguracoes = ConfigurarTela
        self.interfCasCurso = CadastrarCurso
        self.interfReserva = ReservaInterface
        self.interfEditPessoa = EditarPessoas
        self.interfEditArea = EditarArea
        self.interfEditCurso = EditarCurso
        self.interfEditLogin = EditarLogin
        self.interfEditReserva = EditarReserva
        self.interfEditSala = EditarSala

        # Telas dentro do menu para alterar as janelas pelo sub menu
        self.btnPessoa.clicked.connect(lambda: self.trocarTelaMenu(self.cadastros))
        self.btnPessoas.clicked.connect(lambda: self.trocarTelaMenu(self.cadastros))
        self.btnBusca.clicked.connect(lambda: self.trocarTelaMenu(self.busca))
        self.btnPesquisa.clicked.connect(lambda: self.trocarTelaMenu(self.busca))
        self.btnEditarSimples.clicked.connect(lambda: self.trocarTelaMenu(self.editar)) 
        self.btnEditar.clicked.connect(lambda: self.trocarTelaMenu(self.editar)) 

        # Botões da própria interface
        self.btnIncio.clicked.connect(lambda: self.setInterfaceOnHome(self.inicio))
        self.btnHome.clicked.connect(lambda: self.setInterfaceOnHome(self.inicio))
        self.btnHomeAtalho.clicked.connect(lambda: self.setInterfaceOnHome(self.inicio))

        self.btnCadastroLogin.clicked.connect(lambda: self.setInterfaceOnHome(self.interfCasLogin))
        self.btnArea.clicked.connect(lambda: self.setInterfaceOnHome(self.interfCasArea))
        self.btnCadastarSala.clicked.connect(lambda: self.setInterfaceOnHome(self.interfcasSala))
        self.btnCadastroPessoa.clicked.connect(lambda: self.setInterfaceOnHome(self.interfCasPessoa))
        self.btnCurso.clicked.connect(lambda: self.setInterfaceOnHome(self.interfCasCurso))
        self.btnReserva.clicked.connect(lambda: self.setInterfaceOnHome(self.interfReserva))
        self.btnEditarPessoas.clicked.connect(lambda: self.setInterfaceOnHome(self.interfEditPessoa))
        self.btnEditarReserva.clicked.connect(lambda: self.setInterfaceOnHome(self.interfEditReserva))
        self.btnEditarArea.clicked.connect(lambda: self.setInterfaceOnHome(self.interfEditArea))
        self.btnEditaCurso.clicked.connect(lambda: self.setInterfaceOnHome(self.interfEditCurso))
        self.btnEditarLogin.clicked.connect(lambda: self.setInterfaceOnHome(self.interfEditLogin))
        self.btnEditarSala.clicked.connect(lambda: self.setInterfaceOnHome(self.interfEditSala))

        self.btnConfiguracoes.clicked.connect(lambda: self.setInterfaceOnHome(self.interfCongiguracoes))
        self.btnConfig.clicked.connect(lambda: self.setInterfaceOnHome(self.interfCongiguracoes))
        self.btnSair.clicked.connect(self.fazer_logout)
        self.btnSairSimples.clicked.connect(self.fazer_logout)

        self.btnMinimizar.clicked.connect(self.showMinimized)
        self.btnTelaCheia.clicked.connect(self.windowConnect)
        self.btnFecharPagina.clicked.connect(self.close)

    def setInterfaceOnHome(self, interface: QWidget):
        self.container: QStackedWidget
        if type(interface) != QWidget:  # precisa instanciar a interface
            interface = interface()
        if self.container.currentIndex() != 0:
            self.container.removeWidget(self.container.currentWidget())
        if interface != self.inicio:
            self.container.addWidget(interface)
        self.container.setCurrentWidget(interface)

    def windowConnect(self):
        if self.isMaximized():
            self.showNormal()
            self.btnTelaCheia.setStyleSheet("""
                #btnTelaCheia {
                    icon: url("App/view/ui/icones/iconTelaCheia.png"); 
                }""")
        else:
            self.showMaximized()
            self.btnTelaCheia.setStyleSheet("""
                #btnTelaCheia {
                    icon: url("App/view/ui/icones/iconRestaurarTamanhoTela.png"); 
                }""")

    def inserirTelasMenu(self, menu):
        for i in menu:
            self.menuQuebrado.addWidget(i)

    def trocarTela(self, tela):
        self.container.setCurrentWidget(tela)

    def trocarTelaMenu(self, menu):
        if self.subMenuQuebrado.isVisible():
            self.menuQuebrado.setCurrentWidget(menu)
        else:
            self.subMenuQuebrado.show()
            self.menuQuebrado.setCurrentWidget(menu)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.childAt(event.pos()) == self.cabecalho:  
                self.moving = True
                self.offset = event.pos()
            self._resize_direction = self._get_resize_direction(event.pos())
            if self._resize_direction == "bottom-right":
                self._resizing = True
                self._resize_geometry = (self.geometry(), event.globalPos())

    def mouseMoveEvent(self, event):
        if self._resizing:
            self._resize_geometry = (self.geometry(), event.globalPos())
            if not self._resize_timer.isActive():
                self._resize_timer.start(10)
        elif self.moving and not self.isMaximized():
            self.move(self.pos() + event.pos() - self.offset)

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.childAt(event.pos()) == self.cabecalho:  
                if self.isMaximized():
                    self.showNormal()
                    self.btnTelaCheia.setStyleSheet("""
                        #btnTelaCheia {
                            icon: url("App/view/ui/icones/iconTelaCheia.png");
                        }
                    """)
                else:
                    self.showMaximized()
                    self.btnTelaCheia.setStyleSheet("""
                        #btnTelaCheia {
                            icon: url("App/view/ui/icones/iconRestaurarTamanhoTela.png");
                        }""")

    def mouseReleaseEvent(self, event):
        self.moving = False
        self._resizing = False
        self._resize_direction = None
        self.setCursor(Qt.ArrowCursor)

    def _get_resize_direction(self, pos):
        margin = 10
        if pos.x() > self.width() - margin and pos.y() > self.height() - margin:
            self.setCursor(Qt.SizeFDiagCursor)  
            return "bottom-right"
        self.setCursor(Qt.ArrowCursor)  
        return None

    def _apply_resize(self):
        if self._resize_geometry:
            rect, global_pos = self._resize_geometry
            new_width = max(200, global_pos.x() - rect.x())
            new_height = max(200, global_pos.y() - rect.y())
            self.setGeometry(rect.x(), rect.y(), new_width, new_height)

    @pyqtSlot()
    def on_btnFecharMenuQuebrado_clicked(self):
        self.subMenuQuebrado.hide()

    def fazer_logout(self):
        confirmacao = TelaConfirmacao("Tem certeza que deseja sair?", '', "Sim")
        if confirmacao.exec_():
            removerUsuarioLogado()
            self.close()

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    widget = HomePrincipal()
    widget.show()
    app.exec_()
