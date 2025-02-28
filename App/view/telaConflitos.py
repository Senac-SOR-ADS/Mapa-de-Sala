from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi

class TelaConflitos(QDialog):
    def __init__(self, textoConflitos):
        super().__init__()
        loadUi('App/view/ui/telaConflitos.ui', self)
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        # self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.textoConflitos.setText(textoConflitos)
        
        self.btnTelaCheia.clicked.connect(self.windowConnect)
        self.btnFechar.clicked.connect(self.close)
 
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
                                            icon: url("App/view/ui/icones/iconMinimezar.png");
                                            }"""
                                        )