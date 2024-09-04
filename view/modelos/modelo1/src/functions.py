#GUI funções

from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from Custom_Widgets.QCustomTipOverlay import QCustomTipOverlay
from Custom_Widgets.QCustomLoadingIndicators import QCustom3CirclesLoader

from PySide6.QtCore import QSettings, QTimer
from PySide6.QtGui import QColor, QFont, QFontDatabase
from PySide6.QtWidgets import QGraphicsDropShadowEffect

class GuiFunctions():
    def __init__(self, MainWindow):
        self.main = MainWindow
        self.ui = MainWindow.ui

        # Init Tema
        self.initializeAppTheme()

        # Adiciona evento de click na pesquisa 
        self.ui.searchBtn.clicked.connect(self.showSearchResults)
    
    # conecta meu btn
        self.connectMenuButtons()

    # Conecta o botão do menu    
    def connectMenuButtons(self):
        """Conecta os botões para expandir o menu widget"""
        # Expande o centro do menu
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())

        # Fecha o centro do menu
        self.ui.closeCenterMenuBtn.connect(lambda: self.ui.centerMenu())

        # Expande o widget da lateral do menu
        self.ui.notificationBtn.clicked.connect(lambda: self.ui.rightMenu.expandMenu())
        self.ui.moreBtn.clicked.connect(lambda: self.ui.rightMenu.expandMenu())
        self.ui.profileBtn.clicked.connect(lambda: self.ui.rightMenu.expandMenu())

        # Fecha a lateral do menu
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenu.collapseMenu())


    # Cria a pesquisa tooltip
    def createSearchTipOverlay(self):
        """Cria o sistema de pesquisa"""
        tooltip = QCustomTipOverlay(
            title="Procurando resultados",
            description="Procurando...",
            icon=self.main.theme.PATH_RESOURCES+"icon/pesquisar.png", # Icone do tema de pesquisa
            isClosable = True,
            target=self.ui.searchInpContent,
            parent=self.main,
            deleteOnClose = True,
            duration= -1, # Insere a duração para -1 ao auto-close
            tailPosition="top-center",
            closeIcon=self.main.theme.PATH_RESOURCES+"icon/close-center-menu.png", # Adiciona icone de fechar
            toolFlag = True
        )

        # Cria o loading
        loader = QCustom3CirclesLoader(
            parent=self.searchToolTip,
            color=QColor("#333333"), # Cor do tema
            penWidth=20,
            animationDuration=400
        )
        
        # Adiciona o loading ao tipoverlay
        self.searchToolTip.addWidget(loader)
    
    def showSearchResults(self):
        # ...
        searchPhrase = self.ui.searchInp.text()
        # If se é invalido
        if not searchPhrase:
            return
        
        try:
            self.searchToolTip.show()
        except: # Tooltip deletado
            self.createSearchTipOverlay()
            self.searchToolTip.show()

        # Update na descrição da pesquisa
        self.searchToolTip.setDescription("Carregando resultados para: "+searchPhrase)

    # Inicialização tema 
    def initializeAppTheme(self):
        """Inicialize o tema pelas configurações"""
        settings = QSettings()
        current_theme = settings.value("THEME")
        # print("O tema atual é: ", current_theme)

        # Adicionar tema da lista
        self.populateThemeList(current_theme)

        # Conecta o tema alterado e envia um sinal do tema
        self.ui.themeList.currentTextChanged.connect(self.changeAppTheme)

    def populateThemeList(self, current_theme):
        """Temas"""
        theme_count = -1
        for theme in self.ui.themes:
            self.ui.themeList.addItem(theme.name, theme.name)
            # Avalia o tema default
            if theme.defaultTheme or theme.name == current_theme:
                self.ui.themeList.setCurrentIndex(theme_count) # Seleciona o tema

    # Mudar tema
    def changeAppTheme(self):
        """Mudar tema baseada na escolha do usuario"""
        settings = QSettings()
        selected_theme = self.ui.themeList.currentData()
        current_theme = settings.value("THEME")

        if current_theme != selected_theme:
            # Aplicar novo tema
            settings.setValue("THEME", selected_theme)
            QAppSettings.updateAppSettings(self.main, reloadJson=True)


    # Aplicar fonte customizada
    
    def loadProductSansFont(self):
        """carrega e aplica profuct sans font"""
        font_id = QFontDatabase.addApplicationFont("./fonts/google-sans-cufonfonts/ProductSans-Regular.ttf")
        # A fonte não carregada
        if font_id == -1:
            print("Falha no carregamentos da fonte")
            return
        
        # Aplicar fonte
        font_family = QFontDatabase.applicationFontFamilies(font_id)
        if font_family:
            product_sans = QFont(font_family[0])
        else:
            product_sans = QFont("Sans Serif")

        # Aplica na janela principal
        self.main.setFont(product_sans)

        



