import sys
import os
from PyQt6 import *
from PyQt6.uic import loadUi
from PyQt6.QtCore import Qt, QTimer

class interfaceHome(QMainWindow):
    def __init__(self):
        super().__init__()
        try:
            loadUi('', self) #Carregar o arquivo UI

        except Exception as e:
            print(f"Erro ao carregar a interface: {e}")
            sys.exit(1)

#######CONEXÕES SERÃO ADICIONADAS APÓS A CRIAÇÃO DA HOME ORIGINAL#######

if __name__ == "__main__":
    app = QApplication([])
    widget = interfaceHome()
    widget.show()
    app.exec_()