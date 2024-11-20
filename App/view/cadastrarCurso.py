from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer, pyqtSlot
from App.controller.curso import cadastrarCurso
from App.controller.area import listarAreas
from App.controller.utils import validarAcao

#respostas de sucesso e erro = respostas

class CadastrarCurso(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/cadastroCurso.ui',self)
        self.dicionarioDeAreas = listarAreas()
        self.popularJanela()
        
    def popularJanela(self):
        self.comboxArea()
        
    @pyqtSlot()
    def on_btnCadastrarCurso_clicked(self):
        info = self.getCadastroCurso()
        idArea = self.dicionarioDeAreas[info[0]]
        nome, oferta, periodo, carga, horas, alunos = info[1], info[2], info[3], info[4], info[5], info[6]
        if cadastrarCurso(idArea, nome, oferta, periodo, carga, horas, alunos):
            validarAcao()
            
    

    def comboxArea(self):
        areas = self.dicionarioDeAreas.keys()
        self.campoArea.addItems(areas)
            
        
    def getCadastroCurso(self):
        area = self.campoArea.currentText().strip()
        nome = self.nomeCurso.text().strip()
        oferta = self.ofertaCurso.text().strip()
        periodo = self.periodoCurso.currentText().strip()
        carga = self.cargaCurso.text().strip()
        horas = self.horasPorDia.text().strip()
        alunos = self.quantidadeAlunos.text().strip()
        
        return(area, nome, oferta, periodo, carga, horas, alunos)
    
    

    def validandoDados(self):
        self.respostaCadastrando.setText('CADASTRANDO...')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.respostaCadastrando))

    def dadosInvalidos(self):
        texto = 'DADOS INCOMPLETOS.'
        self.respostaCadastroIncompleto.setText(texto)
        QTimer.singleShot(2000, lambda: self.limparCampos(self.respostaCadastroIncompleto))

    def limparCampos(self, campo):
        campo.clear()


