from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from App.controller.sala import atualizarSala, listarSala, buscarSalaId
 
 
class EditarSala(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("App/view/ui/editarSalas.ui",self)
        self.dicionarioDeSala = listarSala()
        self.comboxSala()
        self.nomeSala.currentIndexChanged.connect(self.popularSala)
        self.popularSala()
       
       
    @pyqtSlot()
    def on_cadastrarSala_clicked(self):
        idSala = self.getIdSala()
        info = self.getDadosSala()
        if atualizarSala(info[0], info[1], info[2], info[3], info[4], info[5], idSala):
            print('deu bom')
       
    def comboxSala(self):
        salas = self.dicionarioDeSala.keys()
        self.nomeSala.addItems(salas)
       
    def getIdSala(self):
        salaSelecionada = self.nomeSala.currentText()
        return self.dicionarioDeSala.get(salaSelecionada)
 
    def popularSala(self):
        idSalaCombobox = self.getIdSala()
        info = buscarSalaId(idSalaCombobox)
        nomeSala = info["nome"]
        tipoSala = info["tipo"]
        predio = info["predio"]
        equipamentos = info["equipamentos"]
        capacidade = info["capacidade"]
        obs = info["observacao"]
        if (nomeSala, tipoSala, predio, equipamentos, capacidade, obs):
            self.tipoSala.setCurrentText(tipoSala)
            self.nomePredio.setCurrentText(predio)
            self.tipoEquipamento.setText(equipamentos)
            self.mediaCapacidade.setValue(capacidade)
            self.feedbackText.setText(obs)
           
    def getDadosSala(self):
        nomeSala = self.nomeSala.currentText().strip()
        tipoSala = self.tipoSala.currentText().strip()
        predio = self.nomePredio.currentText().strip()
        equipamentos = self.tipoEquipamento.text().strip()
        capacidade = self.mediaCapacidade.text().strip()
        obs = self.feedbackText.text().strip()
       
        return(nomeSala, tipoSala, predio, equipamentos, capacidade, obs)