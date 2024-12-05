from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class FeadbackConcluido(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/feadbackConcluido.ui',self)
        
    #label do aviso do Concluido = #texto