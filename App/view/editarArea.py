from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from App.controller.area import listarAreas
from App.controller.area import atualizarArea


class EditarArea(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/editarArea.ui',self)
        self.dicionarioDeAreas = listarAreas()
        self.comboxArea()
        self.alterarArea.currentIndexChanged.connect(self.popularArea)
 
    def comboxArea(self):
        areas = self.dicionarioDeAreas.keys()
        self.alterarArea.addItems(areas)
 
    def popularArea(self):
        areaSelecionada = self.alterarArea.currentText()
        if areaSelecionada:
            self.cadastrarArea.setText(areaSelecionada)
 
    @pyqtSlot()
    def on_btnEditarArea_clicked(self):
        nomeArea = self.getEditArea()
        idArea = self.getIdArea()
        if atualizarArea(idArea, nomeArea):
            print('blz!')
        else:
            print('deu erro ai')
 
    def getEditArea(self):
        return self.cadastrarArea.text().strip()
 
    def getIdArea(self):
        areaSelecionada = self.alterarArea.currentText()
        return self.dicionarioDeAreas.get(areaSelecionada)