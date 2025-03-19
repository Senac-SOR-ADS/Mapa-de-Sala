from PyQt5.QtWidgets import QDialog, QDateEdit, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QDate, QTime, pyqtSlot
from App.controller.pessoa import buscarPessoas
from App.controller.sala import listarSala
from App.controller.reserva import getReserva
from App.model.reserva import Reserva
from App.controller.curso import listar_id_e_nome_cursos
from App.controller.utils import modificarData
from App.view.feedback import Feedback

class ReservaUnitaria(QDialog):
    def __init__(self, idReserva, dataReserva):
        super().__init__()
        loadUi('App/view/ui/editarReservaUnitaria.ui',self)
        self.dadosReserva = getReserva(idReserva)
        self.dadosConsultados = {
            'pessoas': buscarPessoas(),
            'salas': listarSala(),
            'cursos': listar_id_e_nome_cursos(),
            'pessoaAtual': self.dadosReserva[2],
            'salaAtual': self.dadosReserva[4],
        }

        self.dataReserva = dataReserva
        self.dadosReserva = getReserva(idReserva)
        self.inicio = self.getHoraFormatada(self.dadosReserva[6])
        self.fim = self.getHoraFormatada(self.dadosReserva[7])
        self.observacao = self.dadosReserva[9]
        self.curso = self.dadosReserva[3]
        self.login = self.dadosReserva[1]
        self.idReserva = idReserva

        self.diaInicio.setCalendarPopup(True)
        self.diaInicio.setDisplayFormat('dd/MM/yyyy')
        self.diaInicio.setMinimumDate(QDate.currentDate())
        self.inicioCurso.timeChanged.connect(self.setMinimoHoraFim)

        # self.popularJanela(self.inicio, self.fim, self.observacao)
        self.comboBoxPessoa()
        self.setCurso()
        self.comboBoxSala()
        self.setDataReserva()
        self.setHoraInicio(self.inicio)
        self.setHoraFim(self.fim)
        self.setMinimoHoraFim()
        self.setObservacao(self.observacao)

        # print("id da reserva", idReserva)
        # print('pessoaAtual', self.dadosReserva[2])
        # print(self.dadosConsultados['pessoas'])

    # def popularJanela(self, horaInicio, horaFim, observacao):
    #     self.comboBoxPessoa()
    #     self.setCurso()
    #     self.comboBoxSala()
    #     self.setHoraInicio(horaInicio)
    #     self.setHoraFim(horaFim)
    #     self.setMinimoHoraFim()
    #     self.setObservacao(observacao)
        
    def get_indice_pessoa_atual(self):
        pessoas = self.dadosConsultados['pessoas']
        for i in range(len(pessoas.keys())):
            if list(pessoas.keys())[i] == self.dadosConsultados['pessoaAtual']:
                # print(f'pessoa atual: ID({i})- Nome({list(pessoas.keys())[i]})')
                return i
        return 0
    
    def get_indice_sala_atual(self):
        salas = self.dadosConsultados['salas']
        salaAtual = self.dadosConsultados['salaAtual']
        indice = list(salas.values()).index(salaAtual)
        return indice

    def comboBoxPessoa(self):
        """Busca as pessoas no banco e popula o comboBox."""
        pessoas = self.dadosConsultados['pessoas'] #buscarPessoas()
        self.nomeDocente.clear()
        self.nomeDocente.addItems(pessoas.values())

        pessoa_atual = self.get_indice_pessoa_atual()
        self.nomeDocente.setCurrentIndex(pessoa_atual)

        # print(f'indice pessoa atual: {pessoa_atual}')
    
    def pegar_docente_selecionado(self):
        docentes = self.dadosConsultados['pessoas']
        indice = self.nomeDocente.currentIndex()
        id = list(docentes.keys())[indice] or 0
        return id
    
    def pegar_sala_selecionada(self):
        salas = self.dadosConsultados['salas']
        indice = self.salaReserva.currentIndex()
        id = list(salas.values())[indice] or 0
        return id
    
    def pegar_hora(self, horaTimedelta):
        stringHoras = str(horaTimedelta)
        hora = int(stringHoras.split(':')[0])
        minuto = int(stringHoras.split(':')[1])
        return f"{hora:02d}:{minuto:02d}"
    
    def pegar_hora_inicio_selecionada(self):
        inicio = self.dadosReserva[6]
        indice = self.inicioCurso.currentIndex()
        id = list(inicio.values())[indice] or 0


    def setCurso(self):
        id_curso = self.curso
        cursos = self.dadosConsultados['cursos']
        self.nomeCurso.clear()
        nomeCurso = cursos[id_curso]
        self.nomeCurso.setText(nomeCurso)
        # print(curso)

    def comboBoxSala(self):
        """Busca as salas no banco e popula o comboBox."""
        salas = self.dadosConsultados['salas']
        self.salaReserva.clear()
        self.salaReserva.addItems(salas.keys())

        sala_atual = self.get_indice_sala_atual()
        self.salaReserva.setCurrentIndex(sala_atual)

    def setDataReserva(self):
        self.diaInicio.setDate(self.dataReserva)
 
    def getHoraFormatada(self, horaTimedelta):
        time = QTime()
        stringHoras = str(horaTimedelta)
        hora = int(stringHoras.split(':')[0])
        minuto = int(stringHoras.split(':')[1])
        time.setHMS(hora, minuto, 0)
        return time
   
    def setHoraInicio(self, horas):
        self.inicioCurso.setTime(horas)
 
    def setHoraFim(self, horas):
        self.fimCurso.setTime(horas)
 
    def setMinimoHoraFim(self):
        time = self.inicioCurso.time()
        self.fimCurso.setMinimumTime(time)
   
    def setObservacao(self, txt):
        self.observacaoReserva.setText(txt)
    def getObservacao(self):
        return self.observacaoReserva.text()

    @pyqtSlot()
    def on_btnEditarReserva_clicked(self):
        login = self.login
        docente = self.pegar_docente_selecionado()
        sala = self.pegar_sala_selecionada()
        diaInicio = modificarData(self.diaInicio.text().strip())
        id_curso = self.curso
        hrInicio = self.inicioCurso.text()
        hrFim = self.fimCurso.text()
        obs = self.getObservacao()

        resultado = Reserva.atualizar(login, docente, id_curso, sala, diaInicio, hrInicio, hrFim, True, obs, self.idReserva)
        if resultado:
            resposta = Feedback(True, 'Atualização efetuado', 'Reserva atualizada', 'atualizado')
            resposta.exec_()
            self.close()
        else:
            resposta = Feedback(False, 'Erro ao Atualizar', 'não atualizado', 'não atualizado')
            resposta.exec_()

