from PyQt5.QtWidgets import QWidget, QDateEdit
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer, QDate, pyqtSlot
from App.model.reserva import Reserva

from App.controller.curso import listarCursos
from App.controller.pessoa import buscaPessoas, modificarData
from App.controller.sala import listarSala
from App.controller.reserva import validarDia

from App.model.login import Login

class ReservaInterface(QWidget):
    curso = listarCursos()
    pessoa = buscaPessoas()
    sala = listarSala()
    
    
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/reserva.ui',self)
        self.popularJanela()

        # Os metodos abaixo servem para transformar o QDateEdit em um calendário
        self.diaInicio = self.findChild(QDateEdit, 'diaInicio') 
        self.diaFim = self.findChild(QDateEdit, 'diaFim')  

        self.diaInicio.setCalendarPopup(True)
        self.diaInicio.setDisplayFormat('dd/MM/yyyy')
        self.diaInicio.setDate(QDate.currentDate())  

        self.diaFim.setCalendarPopup(True)
        self.diaFim.setDisplayFormat('dd/MM/yyyy')
        self.diaFim.setDate(QDate.currentDate()) 

    def getDados(self)->dict:
        """Pegando o dados na interface e retornando os valores"""
        nomeDocenteResponsavel = self.nomeDocente.currentText().strip()
        idDocente = self.pessoa[nomeDocenteResponsavel]
        nomeSala = self.salaReserva.currentText().strip()
        idSala = self.sala[nomeSala]
        nomeCurso = self.cursoReserva.currentText().strip()
        idCurso = self.curso[nomeCurso]
        
        equipamentos = self.equipamentosReserva.text().strip() 
        inicio = modificarData(self.diaInicio.text().strip() )
        fim = modificarData(self.diaFim.text().strip() )
        observacao = self.observacaoReserva.text().strip() 
        cursoInicio = self.inicioCurso.time().toString('HH:mm')
        cursoFim = self.fimCurso.time().toString('HH:mm')
        segunda = self.segCheck.isChecked()        
        terca = self.terCheck.isChecked()
        quarta = self.quaCheck.isChecked()
        quinta = self.quiCheck.isChecked()
        sexta = self.sextaCheck.isChecked()
        sabado = self.sabCheck.isChecked()

        dados = {"idDocente":idDocente, 
                 "idSala":idSala, 
                 "idCurso":idCurso,
                 "equipamentos":equipamentos,
                 "inicio":inicio,
                 "fim":fim,
                 "observações":observacao,
                 "inicioCurso":cursoInicio,
                 "fimCurso":cursoFim,
                 "seg":segunda,
                 "ter":terca,
                 "qua":quarta,
                 "qui":quinta,
                 "sexta":sexta,
                 "sab":sabado}
        return dados
    
    @pyqtSlot()
    def on_btnFazerReserva_clicked(self):
        info = self.getDados()
        idLogin = 8
        # if Reserva(idLogin, info).fazer_reserva():
        #     print('ok')
        # dados = self.getDados()
        # DataInicio = dados["inicio"]
        # DataFim = dados["fim"]
        # diasValidos = (dados['seg'], dados['ter'], dados['qua'], dados['qui'], dados['sexta'], dados['sab'], False)
        # validarDia(DataInicio, DataFim, diasValidos)
        if Reserva(idLogin, info['idDocente'], info['idCurso'], info['idSala'], info['inicio'], info['inicioCurso'], info['fimCurso'], info['observações']).fazer_reserva():
            print('reservado com sucesso')
        else:
            print('Erro ao reservar')
        

    def popularJanela(self):
        self.comboBoxCurso()
        self.comboBoxPessoa()
        self.comboBoxSala()

    def comboBoxCurso(self):
        self.cursoReserva.addItems(self.curso.keys())

    def comboBoxPessoa(self):
        self.nomeDocente.addItems(self.pessoa.keys())

    def comboBoxSala(self):
        self.salaReserva.addItems(self.sala.keys())

    def testeDias(self):
        diaInicio = self.getDados().values()
        print(diaInicio)
        validarDia()
        
        
    

        
    def validandoDados(self):
        self.feedbackReserva.setText('Reserva realizada.')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.feedbackReserva))

    def dadosInvalidos(self):
        self.feedbackReserva.setText('Dados incomoletos.')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.feedbackReserva))

    def limparCampos(self, campo):
        campo.clear()