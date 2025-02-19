from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
 
class CardPesquisa(QWidget):
    def __init__(self, dados_modelReserva, dicionarioSalas:dict):
        super().__init__()
        loadUi('App/view/ui/cardPesquisa.ui',self)
        self.label_6.setText(dados_modelReserva.get_dia().__str__())
        inicio = int(dados_modelReserva.get_horaInicio().__str__().split(':')[0])
        for chave, valor in dicionarioSalas.items():
            if valor == dados_modelReserva.get_idSala():
                self.nomeSALA = chave
                break
        self.label_9.setText(str(self.nomeSALA))
        if inicio < 12:
            print('manha')
        elif inicio < 18:
            print('tarde')
        else:
            print('noite')
