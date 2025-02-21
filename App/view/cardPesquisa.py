from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QUrl
from os.path import join, dirname, realpath
from PyQt5.QtGui import QPixmap

 
class CardPesquisa(QWidget):
    CURRENT_DIR = dirname(realpath(__file__))

    def __init__(self, dados_modelReserva, dicionarioSalas:dict, dicionarioCursos:dict):
        super().__init__()
        loadUi('App/view/ui/cardPesquisa.ui',self)
        self.label_6.setText(dados_modelReserva.get_dia().__str__())
        inicio = int(dados_modelReserva.get_horaInicio().__str__().split(':')[0])
        # url = QUrl.fromLocalFile(filename)
        "App/view/ui/css/cards/manha.css"
        "App/view/ui/css/cards/noite.css"
        "App/view/ui/css/cards/tarde.css"
        if inicio < 12:
            cssFile = join(self.CURRENT_DIR, "./ui/css/cards/manha.css")
            icone = join(self.CURRENT_DIR, r"./ui/icones/iconManha.png")
        elif inicio < 18:
            cssFile = join(self.CURRENT_DIR, "./ui/css/cards/tarde.css")
            icone = join(self.CURRENT_DIR, r"./ui/icones/iconTarde.png")
        else:
            cssFile = join(self.CURRENT_DIR, "./ui/css/cards/noite.css")
            icone = join(self.CURRENT_DIR, r"./ui/icones/iconNoite.png")
        with open(cssFile, 'r') as css:
            self.setStyleSheet(css.read())
            self.iconePeriodo.setPixmap(QPixmap(icone))

        for chave, valor in dicionarioSalas.items():
            if valor == dados_modelReserva.get_idSala():
                self.nomeSALA = chave
                break
        for chave, valor in dicionarioCursos.items():
            if valor == dados_modelReserva.get_idCurso():
                self.oferta = chave
                break
        self.label_9.setText(str(self.nomeSALA))
        self.label_8.setText(str(self.oferta))
        
