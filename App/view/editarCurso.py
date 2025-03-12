from PyQt5.QtWidgets import QWidget, QDateTimeEdit
from PyQt5.QtCore import QTimer, pyqtSlot, QDate, QTime
from datetime import datetime, timedelta
from App.controller.curso import listarCurso, lista_de_cursos, buscarCursosId, atualizarCurso
from App.model.curso import *
from App.controller.area import listarAreas
from App.controller.utils import erroEdicao, sucessoEdicao

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
            sucessoEdicao(self)
            self.setIndexInicial()
            return True
        erroEdicao(self)
        return False

    def comboOferta(self):
        dados = self.dicionarioDeCursos.values()
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
            self.horasPorDia.setTime(horasDia)
            self.quantidadeAlunos.setValue(int(qtdAlunos))
    
    def obterDateTime(self, horasCurso:timedelta):
        time = QTime()
        stringHoras = str(horasCurso)
        hora = int(stringHoras.split(':')[0])
        minuto = int(stringHoras.split(':')[1])
        time.setHMS(hora, minuto, 0)
        return time

    def getEditarCurso(self):
        area = self.getIdArea()
        nome = self.nomeCurso.text().strip()
        oferta = self.getIdOferta()
        periodo = self.periodoCurso.currentText().strip()
        carga = self.cargaCurso.text().strip()
        horas = self.horasPorDia.text().strip()
        alunos = self.quantidadeAlunos.text().strip()
        return(area, nome, oferta, periodo, carga, horas, alunos)
    
    def getIdArea(self):
        area = self.campoArea.currentText()
        return self.dicionarioDeAreas.get(area)

    def getIdOferta(self):
        oferta = self.ofertaCurso.currentIndex()
        return list(self.dicionarioDeCursos.keys())[oferta]
    
    
    def setIndexInicial(self):
            self.ofertaCurso.setCurrentIndex(0)
 