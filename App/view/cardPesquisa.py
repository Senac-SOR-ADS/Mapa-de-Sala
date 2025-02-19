from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
 
class CardPesquisa(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/cardPesquisa.ui',self)