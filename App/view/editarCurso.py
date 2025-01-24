from PyQt5.QtWidgets import QWidget, QDateTimeEdit
from PyQt5.QtCore import QTimer, pyqtSlot, QDate, QTime
from datetime import datetime, timedelta
from App.controller.curso import listarCurso, buscarCursosId, atualizarCurso
from App.model.curso import *
from App.controller.area import listarAreas

from PyQt5.uic import loadUi


class EditarCurso(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/editarCurso.ui',self)
        self.dicionarioDeCursos = listarCurso()
        self.dicionarioDeAreas = listarAreas()
        if (self.ofertaCurso.currentIndexChanged.connect(self.popularCurso)):
            self.popularJanela()

    def popularJanela(self):
        self.comboOferta()
        self.comboArea()

    @pyqtSlot()
    def on_btnEditarCurso_clicked(self):
        idCurso = self.getIdOferta()
        infos = self.getEditarCurso()

        if(Curso.atualizar(idCurso, infos[0], infos[1], infos[2], infos[3], infos[4], infos[5], infos[6])):
            print("Curso atualizado - editarCurso view")
            return True
        return False

    def comboOferta(self):
        dados = self.dicionarioDeCursos.keys()
        self.ofertaCurso.addItems(dados)

    def comboArea(self):
        dados = self.dicionarioDeAreas.keys()
        self.campoArea.addItems(dados)

    def popularCurso(self):
        idCurso = self.getIdOferta()
        info = buscarCursosId(idCurso)
        nome = info['nome']
        cargaHoraria = info['cargaHoraria']
        periodo = info['periodo']
        area = info['idArea']
        horasDia = self.obterDateTime(info['horasDia'])
        qtdAlunos = info['qtdAlunos']

        if (nome, cargaHoraria, periodo, area, horasDia, qtdAlunos):
            self.nomeCurso.setText(nome)
            self.cargaCurso.setValue(cargaHoraria)
            self.periodoCurso.setCurrentText(periodo)
            self.campoArea.setCurrentText(area)
            self.horasPorDia.setDateTime(horasDia)
            self.quantidadeAlunos.setValue(int(qtdAlunos))
    
    def obterDateTime(self, horas:timedelta):
        horas = int(horas.total_seconds())
        time = self.horasPorDia.dateTime().addSecs(horas)
        return time


    # def limparCampos(self):
    #     idCurso = self.getIdOferta()
    #     print(idCurso)
    #     info = buscarCursosId(idCurso)
    #     nome = info['nome']
    #     cargaHoraria = info['cargaHoraria']
    #     periodo = info['periodo']
    #     area = info['idArea']
    #     horasDia = info['horasDia']
    #     qtdAlunos = info['qtdAlunos']

    #     if (nome, cargaHoraria, periodo, area, horasDia, qtdAlunos):
    #         self.nomeCurso.clear()
    #         self.cargaCurso.clear()
    #         self.periodoCurso.clear()
    #         self.campoArea.clear()
    #         self.horasPorDia.clear()
    #         self.quantidadeAlunos.clear()

    def getEditarCurso(self):
        oferta = self.ofertaCurso.currentText().strip()
        nome = self.nomeCurso.text().strip()
        area = self.getIdArea()
        periodo = self.periodoCurso.currentText().strip()
        carga = self.cargaCurso.text().strip()
        horas = self.horasPorDia.text().strip()
        alunos = self.quantidadeAlunos.text().strip()
        return(area, nome, oferta, periodo, carga, horas, alunos)
    
    def getIdArea(self):
        area = self.campoArea.currentText()
        print(f"Get id area: {self.dicionarioDeAreas.get(area)}")
        return self.dicionarioDeAreas.get(area)

    def getIdOferta(self):
        oferta = self.ofertaCurso.currentText()
        return self.dicionarioDeCursos.get(oferta)
    
    
