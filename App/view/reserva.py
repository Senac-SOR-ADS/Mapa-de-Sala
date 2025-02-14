
from PyQt5.QtWidgets import QWidget, QDateEdit, QComboBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer, QDate, QTime, pyqtSlot

# from App.model.reserva import Reserva
# from App.model.login import Login
# Não está sendo utilizado no arquivo

from App.view.telaConfirmacao import TelaConfirmacao

from App.controller.curso import listarCurso, buscarCursoId, lista_de_cursos
from App.controller.pessoa import buscarPessoas
from App.controller.sala import listarSala
from App.controller.utils import modificarData, modificarDataReserva
from App.controller.reserva import validarCadastro, validarDiaSemana, realizar_reserva_no_dia
from App.controller.login import pegarUsuarioLogado


class ReservaInterface(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/reserva.ui',self)
        self.dadosConsultados = {
            'pessoas': buscarPessoas(),
            'salas': listarSala(),
            #'cursos': listarCurso(),
            'cursos': lista_de_cursos()
        }

        self.comboBoxOferta()
        self.comboBoxPessoa()
        self.comboBoxSala()
        self.setPeriodos(0)
        self.selecionarOferta()

        # Os metodos abaixo servem para transformar o QDateEdit em um calendário
        self.diaInicio = self.findChild(QDateEdit, 'diaInicio') 
        self.diaFim = self.findChild(QDateEdit, 'diaFim')

        self.diaInicio.setCalendarPopup(True)
        self.diaInicio.setDisplayFormat('dd/MM/yyyy')
        self.diaInicio.setDate(QDate.currentDate())
        self.diaFim.setCalendarPopup(True)
        self.diaFim.setDisplayFormat('dd/MM/yyyy')
        self.diaFim.setDate(QDate.currentDate())
        self.setDataMinima()
        
        self.diaInicio.dateChanged.connect(self.setDataMinima)
        self.inicioCurso.timeChanged.connect(self.setIntervaloHoras)
        self.cursoReserva.currentIndexChanged.connect(self.selecionarOferta)

        self.checkFrame.setStyleSheet("""
            QCheckBox::indicator {
                width: 30px;
                height: 30px;
            }
            QCheckBox::indicator:unchecked {
                image: url("App/view/ui/icones/iconCheckLaranja.png");
            }
            QCheckBox::indicator:checked {
                image: url("App/view/ui/icones/iconCheckAtivo.png");
            }
        """)
        

    def getDados(self)->dict:
        """Pegando o dados na interface e retornando os valores"""
        pessoas = buscarPessoas()
        sala = listarSala()
        curso = listarCurso() 
        nomeDocenteResponsavel = self.nomeDocente.currentText().strip()
        idDocente = pessoas[nomeDocenteResponsavel]
        nomeSala = self.salaReserva.currentText().strip()
        idSala = sala[nomeSala]
        nomeCurso = self.cursoReserva.currentText().strip()
        idCurso = curso[nomeCurso]
        
        
        equipamentos = self.equipamentosReserva.text().strip() 
        diaInicio = modificarData(self.diaInicio.text().strip() )
        diaFim = modificarData(self.diaFim.text().strip() )
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
                 "diaInicio":diaInicio,
                 "diaFim":diaFim,
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
        idLogin = pegarUsuarioLogado()
        diasValidos = (info['seg'], info['ter'], info['qua'], info['qui'], info['sexta'], info['sab'], False)
        if validarDiaSemana(info['diaInicio'], diasValidos):
            dias_livres, dias_ocupados = validarCadastro(info, diasValidos)

            if dias_livres and dias_ocupados:
                #fazer a pergunta se quer cadastrar mesmo assim
                txt = ''
                for dia, reserva in dias_ocupados.items():
                    txt += f'{dia} | {reserva[1][2]} - {reserva[1][3]}\n'
                    
                confirmacao = TelaConfirmacao( 'Conflitos', txt, 'Confirmar')
                if confirmacao.exec_():
                    realizar_reserva_no_dia(idLogin.get('id_login'), info, dias_livres)
                    print('Reserva feita com sucesso!')
                    return
                else:
                    print('Não foi possível fazer a reserva, já existe uma reserva nesse horário')

            elif dias_livres and not dias_ocupados:
                # fazer reserva direto
                realizar_reserva_no_dia(idLogin.get('id_login'), info, dias_livres)
                print('Reserva feita com sucesso!')

            elif not dias_livres:
                # mostrar que nao tem dias disponiveis para reserva
                print('ninhum dia disponivel para reserva')

        return
    
    
    def setDataMinima(self):
        """Define a data mínima de término da reserva"""
        primeiroDia = self.diaInicio.date()
        self.diaFim.setMinimumDate(primeiroDia)
    
    def setMinimoFim(self):
        """Define o horário mínimo para acabar a reserva"""
        horarioComeco = self.inicioCurso.time()
        self.fimCurso.setMinimumTime(horarioComeco)


    def comboBoxOferta(self):
        ofertas = [curso.get_oferta() for curso in self.dadosConsultados['cursos'] ]
        self.cursoReserva.clear()
        self.cursoReserva.addItems(ofertas)
    
    
    def comboBoxPessoa(self):
        """Busca as pessoas no banco e popula o comboBox."""
        pessoas = self.dadosConsultados['pessoas']#buscarPessoas()
        self.nomeDocente.clear()
        self.nomeDocente.addItems(pessoas.keys())

    def comboBoxSala(self):
        """Busca as salas no banco e popula o comboBox."""
        salas = self.dadosConsultados['salas']#listarSala()
        self.salaReserva.clear()
        self.salaReserva.addItems(salas.keys())

    # selecionar curso com base no valor da oferta selecionada
    def selecionarOferta(self):
        idx = self.cursoReserva.currentIndex()
        nome_curso = self.dadosConsultados['cursos'][idx].get_nome()
        self.nomeCurso.setText(nome_curso)
        self.setPeriodos(idx)

    def setPeriodos(self, indice):
        """Verifica o período e depois define os horários"""
        curso = self.dadosConsultados['cursos'][indice]
        periodo = curso.get_periodo()
        intervalo = {'Manha': (8,0,0), 'Tarde': (13,30,0), 'Noite': (19,0,0)}[periodo]
        horas = QTime()
        horas.setHMS(*intervalo)
        self.inicioCurso.setTime(horas)
        self.setIntervaloHoras()

    def setIntervaloHoras(self):
        self.setMinimoFim()
        indice = self.cursoReserva.currentIndex()
        curso = self.dadosConsultados['cursos'][indice]
        horasDia = curso.get_horasDia().__str__().split(':')
        horas = QTime()
        horaInicio = self.getHoraInicio()
        horas.setHMS(horaInicio.hour(), horaInicio.minute(), 0)
        horas.setHMS(horas.hour() + int(horasDia[0]), horas.minute(), 0)
        self.fimCurso.setTime(horas)

    def getPeriodoCurso(self):
        """Retorna o período do curso"""
        idCurso = self.getIdCurso()
        dados = buscarCursoId(idCurso)
        periodo = dados.get('periodo')
        return periodo

    def getHoraInicio(self):
        """Retorna a hora de ínicio"""
        horaInicio = self.inicioCurso.time()
        return horaInicio

    def getHorasCurso(self, hora):
        """Retorna às horas diarias do curso"""
        idCurso = self.getIdCurso()
        dados = buscarCursoId(idCurso)
        horasDia = dados.get('horasDia')
        numero = horasDia.__str__()
        hora = numero.split(':')[0]
        return int(hora)
    
    def getIdCurso(self):
        """Retorna o id do curso"""
        dados = self.getDados()
        curso = dados.get('idCurso')
        return curso

    def setHoraInicio(self, hora):
        """Define a hora de início"""
        self.inicioCurso.setTime(hora)

    def setHoraFim(self, hora):
        """Define a hora de fim"""
        self.fimCurso.setTime(hora)
    
    def validandoDados(self):
        self.feedbackReserva.setText('Reserva realizada.')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.feedbackReserva))

    def dadosInvalidos(self):
        self.feedbackReserva.setText('Dados incomoletos.')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.feedbackReserva))

    def limparCampos(self, campo):
        campo.clear()
