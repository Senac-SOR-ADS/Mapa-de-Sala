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

        
        #btn de editar = btnEditarArea
        #combobox editar = editarArea
        
    def comboxArea(self):
        areas = self.dicionarioDeAreas.keys()
        self.alterarArea.addItems(areas)
        
        
        #pegar id area para mudar
    def getIdAra(self):
        idArea = self.dicionarioDeAreas.values()
        return idArea
        
        
        #popular lineedit
    def popularArea(self):
        area = self.dicionarioDeAreas.values()
        print(area)
        
    @pyqtSlot()
    def on_btnEditarArea_clicked(self):
        nomeArea = self.getEditArea()
        idArea = self.getIdAra()
        if atualizarArea(idArea, nomeArea):
            print('blz')
        print('bla bla bla')

    
    def getEditArea(self):
        area = self.alterarArea.currentText().strip()
        return area
    