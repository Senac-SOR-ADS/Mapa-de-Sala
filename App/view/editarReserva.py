from PyQt5.QtWidgets import QWidget, QDateEdit
from PyQt5.QtCore import QDate, QTime, pyqtSlot
from PyQt5.uic import loadUi

from App.view.telaConfirmacao import TelaConfirmacao

from App.controller.curso import listarCurso, buscarCursoId
from App.controller.pessoa import buscarPessoas
from App.controller.sala import listarSala
from App.controller.utils import modificarData
from App.controller.reserva import validarCadastro, validarDiaSemana, realizar_reserva_no_dia
from App.controller.login import pegarUsuarioLogado

class EditarReserva(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/editarReserva.ui',self)
        self.popularJanela()
        
        #btn editar reserva = btnEditarReserva

        self.diaInicio = self.findChild(QDateEdit, 'diaInicio') 
        self.diaFim = self.findChild(QDateEdit, 'diaFim')

        self.diaInicio.setCalendarPopup(True)
        self.diaInicio.setDisplayFormat('dd/MM/yyyy')
        self.diaInicio.setDate(QDate.currentDate())

        self.setDataMinima()
        self.setHorarioMinimo()
        self.setPeriodos()

        self.diaInicio.dateChanged.connect(self.setDataMinima)
        self.inicioCurso.timeChanged.connect(self.setHorarios)
        self.cursoReserva.currentIndexChanged.connect(self.setPeriodos)

        self.diaFim.setCalendarPopup(True)
        self.diaFim.setDisplayFormat('dd/MM/yyyy')
        self.diaFim.setDate(QDate.currentDate())

    def getDados(self):
        """Pegando o dados na interface e retornando os valores"""
        pessoas = buscarPessoas()
        sala = listarSala()
        curso = listarCurso()
        nomeDocenteResponsavel = self.nomeDocente.currentText().strip()
        nomeSala = self.salaReserva.currentText().strip()
        nomeCurso = self.cursoReserva.currentText().strip()

        idDocente = pessoas[nomeDocenteResponsavel]
        idSala = sala[nomeSala]
        idCurso = curso[nomeCurso]

        equipamentos = self.equipamentosReserva.text().strip()
        diaInicio = modificarData(self.diaInicio.text().strip())
        diaFim = modificarData(self.diaFim.text().strip())
        observacao = self.observacaoReserva.text().strip()
        horarioInicio = self.inicioCurso.time().toString('HH:mm')
        horarioFim = self.fimCurso.time().toString('HH:mm')
        segunda = self.segCheck.isChecked()        
        terca = self.terCheck.isChecked()
        quarta = self.quaCheck.isChecked()
        quinta = self.quiCheck.isChecked()
        sexta = self.sextaCheck.isChecked()
        sabado = self.sabCheck.isChecked()

        dados = {"idDocente": idDocente,
                 "idSala": idSala,
                 "idCurso": idCurso,
                 "equipamentos": equipamentos,
                 "diaInicio": diaInicio,
                 "diaFim": diaFim,
                 "observações": observacao,
                 "inicioCurso": horarioInicio,
                 "fimCurso": horarioFim,
                 "seg": segunda,
                 "ter": terca,
                 "qua": quarta,
                 "qui": quinta,
                 "sexta": sexta,
                 "sab": sabado}
        return dados
    
    def popularJanela(self):
        """Popula os comboBoxes com dados do banco."""
        self.comboBoxCurso()
        self.comboBoxPessoa()
        self.comboBoxSala()

    def comboBoxCurso(self):
        cursos = listarCurso()
        self.cursoReserva.clear()
        self.cursoReserva.addItems(cursos.keys())

    def comboBoxPessoa(self):
        """Busca as pessoas no banco e popula o comboBox."""
        pessoas = buscarPessoas()
        self.nomeDocente.clear()
        self.nomeDocente.addItems(pessoas.keys())

    def comboBoxSala(self):
        """Busca as salas no banco e popula o comboBox."""
        salas = listarSala()
        self.salaReserva.clear()
        self.salaReserva.addItems(salas.keys())

    def getIdCurso(self):
        """Retorna o id do curso"""
        dados = self.getDados()
        curso = dados.get('idCurso')
        return curso
    
    def getHorasCurso(self):
        """Retorna às horas diarias do curso"""
        idCurso = self.getIdCurso()
        dados = buscarCursoId(idCurso)
        horasDia = dados.get('horasDia')
        numero = horasDia.__str__()
        hora = numero.split(':')[0]
        return int(hora)
    
    def getHoraInicio(self):
        """Retorna a hora de ínicio"""
        horaInicio = self.inicioCurso.time()
        return horaInicio
    
    def getPeriodoCurso(self):
        """Retorna o período do curso"""
        idCurso = self.getIdCurso()
        dados = buscarCursoId(idCurso)
        periodo = dados.get('periodo')
        return periodo
    
    def setDataMinima(self):
        """Define a data mínima de término da reserva"""
        dataMinima = self.diaInicio.date()
        self.diaFim.setMinimumDate(dataMinima)

    def setHorarioMinimo(self):
        """Define o horário mínimo do término da reserva"""
        horarioMinimo = self.inicioCurso.time()
        self.fimCurso.setMinimumTime(horarioMinimo)

    def setPeriodos(self):
        """Verifica o período e depois define os horários"""
        periodo = self.getPeriodoCurso()
        horasDia = self.getHorasCurso()
        intervalo = {'Manhã': (8,0,0), 'Tarde': (13,30,0), 'Noite': (19,0,0)}
        horas = QTime()
        horas.setHMS(*intervalo[periodo])
        self.setHoraInicio(horas)
        self.setHorarioMinimo()
        horas.setHMS(horas.hour() + horasDia, horas.minute(), 0)
        self.setHoraFim(horas)

    def setIntervalo(self):
        horasDia = self.getHorasCurso()
        intervalo = QTime()
        horaInicio = self.getHoraInicio()
        intervalo.setHMS(horaInicio.hour(), horaInicio.minute(), 0)
        intervalo.setHMS(intervalo.hour() + horasDia, intervalo.minute(), 0)
        self.setHoraFim(intervalo)

    def setHoraInicio(self, hora):
        """Define a hora de início"""
        self.inicioCurso.setTime(hora)

    def setHoraFim(self, hora):
        """Define a hora de fim"""
        self.fimCurso.setTime(hora)

    def setIntervalo(self):
        horasDia = self.getHorasCurso()
        intervalo = QTime()
        horaInicio = self.getHoraInicio()
        intervalo.setHMS(horaInicio.hour(), horaInicio.minute(), 0)
        intervalo.setHMS(intervalo.hour() + horasDia, intervalo.minute(), 0)
        self.setHoraFim(intervalo)

    def setHorarios(self):
        self.setHorarioMinimo()
        self.setIntervalo()