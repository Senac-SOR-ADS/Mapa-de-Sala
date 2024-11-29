from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QStackedWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, pyqtSlot

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


class HomePrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/home.ui',self)
        self.moving = False
        self.subMenuLateral.hide()
        self.subMenuQuebrado.hide()
        self.btnHome.setChecked(True)
        
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

        
    #Telas dentro do menu para alterar as janelas pelo sub menu
        self.btnPessoa.clicked.connect(lambda: self.trocarTelaMenu(self.cadastros))
        self.btnPessoas.clicked.connect(lambda: self.trocarTelaMenu(self.cadastros))
        self.btnBusca.clicked.connect(lambda: self.trocarTelaMenu(self.busca))
        self.btnPesquisa.clicked.connect(lambda: self.trocarTelaMenu(self.busca))
        self.btnEditarSimples.clicked.connect(lambda: self.trocarTelaMenu(self.editar)) 
        self.btnEditar.clicked.connect(lambda: self.trocarTelaMenu(self.editar)) 
        
    #btns da propria interface
    
        # Forma Corrigida para Setar Interface
        #######################################
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
        #######################################

        self.btnMinimizar.clicked.connect(self.showMinimized)
        self.btnFecharPagina.clicked.connect(self.close)
        self.btnTelaCheia.clicked.connect(self.windowConnect)
        
    ################################
    # Função correta para inserir interface
    def setInterfaceOnHome(self, interface:QWidget):
        self.container: QStackedWidget
        if type(interface) != QWidget: # precisa instanciar a interface
            interface = interface()
        if self.container.currentIndex() != 0:
            self.container.removeWidget(self.container.currentWidget())
        if interface != self.inicio:
            self.container.addWidget(interface)
        self.container.setCurrentWidget(interface)

    ################################

    # Faz o botão de Tela Cheia ao ser executado, retornar ao normal
    def windowConnect(self):
        if self.isMaximized():
            self.showNormal()
            self.btnTelaCheia.setStyleSheet("""
                                       #btnTelaCheia {
                                           icon: url("App/view/ui/icones/iconTelaCheia.png"); 
                                        }"""
                                    )
        else:
            self.showMaximized()
            self.btnTelaCheia.setStyleSheet("""
                                       #btnTelaCheia {
                                           icon: url("App/view/ui/icones/iconRestaurarTamanhoTela.png"); 
                                        }"""
                                    )

    
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
        if self.moving and not self.isMaximized():
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
 