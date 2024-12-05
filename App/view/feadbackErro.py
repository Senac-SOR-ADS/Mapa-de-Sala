from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class FeadbackErro(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/feadbackErro.ui',self)
        
    #label do aviso do erro = #texto