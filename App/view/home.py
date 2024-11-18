from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QStackedWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, pyqtSlot
from .cadastroPessoas import cadastroPessoas
from .reserva import ReservaInterface
from .cadastrarArea import CadastrarArea
from .cadastrarCurso import CadastrarCurso
from .cadastrarLogin import CadastroLogin
from .cadastrarSalas import CadastrarSalas
from .configurarTela import ConfigurarTela
from .editarArea import EditarArea
from .editarCurso import EditarCurso
from .editarLogin import EditarLogin
from .editarReserva import EditarReserva
from .editarPessoas import EditarPessoas


class HomePrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/home.ui',self)
        self.moving = False
        self.subMenuLateral.hide()
        self.subMenuQuebrado.hide()
        
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

   # Criando instancias das interfaces
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.interfCasPessoa = cadastroPessoas()
        self.interfReserva = ReservaInterface()
        self.interfCasArea = CadastrarArea()
        self.interfCasCurso = CadastrarCurso()
        self.interfCasLogin = CadastroLogin()
        self.interfcasSala = CadastrarSalas()
        self.interfEditArea = EditarArea()
        self.interfEditCurso = EditarCurso()
        self.interfEditLogin = EditarLogin()
        self.interfEditReserva = EditarReserva()
        self.interfEditPessoas = EditarPessoas()
        self.interfCongiguracoes = ConfigurarTela()
        self.inserirTelas( [self.interfcasSala, self.interfCasPessoa, self.interfReserva, self.interfCasArea, self.interfCasCurso, self.interfCasLogin, self.interfCongiguracoes, self.interfEditArea, self.interfEditCurso, self.interfEditLogin, self.interfEditReserva, self.interfEditPessoas] )
        
    #Telas dentro do menu para alterar as janelas pelo sub menu
        self.btnPessoa.clicked.connect(lambda: self.trocarTelaMenu(self.cadastros))
        self.btnPessoas.clicked.connect(lambda: self.trocarTelaMenu(self.cadastros))
        self.btnBusca.clicked.connect(lambda: self.trocarTelaMenu(self.busca))
        self.btnPesquisa.clicked.connect(lambda: self.trocarTelaMenu(self.busca))
        self.btnEditarSimples.clicked.connect(lambda: self.trocarTelaMenu(self.editar)) 
        self.btnEditar.clicked.connect(lambda: self.trocarTelaMenu(self.editar)) 
        
    #btns da propria interface   
        self.btnEditarArea.clicked.connect(lambda: self.trocarTela(self.interfEditArea))
        self.btnEditaCurso.clicked.connect(lambda: self.trocarTela(self.interfEditCurso))
        self.btnEditarLogin.clicked.connect(lambda: self.trocarTela(self.interfEditLogin))
        self.btnEditarReserva.clicked.connect(lambda: self.trocarTela(self.interfEditReserva))
        self.btnEditarPessoas.clicked.connect(lambda: self.trocarTela(self.interfEditPessoas))
        self.btnCadastarSala.clicked.connect(lambda: self.trocarTela(self.interfcasSala))
        self.btnCadastroPessoa.clicked.connect(lambda: self.trocarTela(self.interfCasPessoa))
        self.btnReserva.clicked.connect(lambda: self.trocarTela(self.interfReserva))
        self.btnIncio.clicked.connect(lambda: self.container.setCurrentWidget(self.inicio))
        self.btnHome.clicked.connect(lambda: self.container.setCurrentWidget(self.inicio))
        self.btnArea.clicked.connect(lambda: self.container.setCurrentWidget(self.interfCasArea))
        self.btnCurso.clicked.connect(lambda: self.container.setCurrentWidget(self.interfCasCurso))
        self.btnCadastroLogin.clicked.connect(lambda: self.container.setCurrentWidget(self.interfCasLogin))
        self.btnConfiguracoes.clicked.connect(lambda: self.container.setCurrentWidget(self.interfCongiguracoes))
        self.btnConfig.clicked.connect(lambda: self.container.setCurrentWidget(self.interfCongiguracoes))
        self.btnMinimizar.clicked.connect(self.showMinimized)
        self.btnFecharPagina.clicked.connect(self.close)
        self.btnTelaCheia.clicked.connect(self.windowConnect)
        
    # Faz o botão de Tela Cheia ao ser executado, retornar ao normal
    def windowConnect(self):
        if self.isMaximized():
            self.showNormal()
            self.btnTelaCheia.setStyleSheet("""
                                       #btnTelaCheia {
                                           icon: url("App/view/ui/icones/square-rounded-regular-24.png"); 
                                        }"""
                                    )
        else:
            self.showMaximized()
            self.btnTelaCheia.setStyleSheet("""
                                       #btnTelaCheia {
                                           icon: url("App/view/ui/icones/select_window_2_24dp_000000_FILL0_wght400_GRAD0_opsz24.png"); 
                                        }"""
                                    )

    def inserirTelas(self, telas):
        for interface in telas:
            self.container.addWidget(interface)
    
    def inserirTelasMenu(self, menu):
        for i in menu:
            self.menuQuebrado.addWidget(i)

    def trocarTela(self, tela):
        """Função para trocar as tela. Necessario
        passar a classe da tela"""
        
        self.container.setCurrentWidget(tela)
    
    def trocarTelaMenu(self, menu):
        if self.subMenuQuebrado.isVisible():
            self.menuQuebrado.setCurrentWidget(menu)
        else:
            self.subMenuQuebrado.show()
            self.menuQuebrado.setCurrentWidget(menu)
            

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
    def on_btnFecharMenuQuebrado_clicked(self):
        self.subMenuQuebrado.hide()
        
        
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    widget = HomePrincipal()
    widget.show()
    app.exec_()
 