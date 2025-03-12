from PyQt5.QtWidgets import QWidget, QComboBox, QLineEdit, QDateEdit
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate, pyqtSlot
from App.controller.pessoa import buscarPessoas, buscarPessoaId, atualizarPessoa
from App.controller.utils import validarInputs, erroEdicao, sucessoEdicao
ID_PESSOA = 0

class EditarPessoas(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/editarPessoa.ui',self)
        self.nomePessoas = self.findChild(QComboBox, 'nomePessoas')
        self.cargo = self.findChild(QComboBox, 'cargo')
        self.email = self.findChild(QLineEdit, 'email')
        self.dataDeNascimento = self.findChild(QDateEdit, 'dataDeNascimento')
        self.dicionarioPessoas = buscarPessoas()
        self.popularJanela()
        self.nomePessoas.currentIndexChanged.connect(self.popularCampos)

        self.dataDeNascimento.setCalendarPopup(True)
        self.dataDeNascimento.setDisplayFormat('dd/MM/yyyy')
        self.dataDeNascimento.setDate(QDate.currentDate())
        

    @pyqtSlot()
    def on_btnEditar_clicked(self):
        dados = self.getValores()
        if validarInputs(dados):
            if atualizarPessoa(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], dados[6]):
                sucessoEdicao(self)
                self.setIndexInicial()
        else:
            erroEdicao(self)
    def popularNomes(self):
        pessoas = self.dicionarioPessoas.values()
        self.nomePessoas.addItems(pessoas)
    
    def popularJanela(self):
        self.popularNomes()
        self.popularCampos()

    def getValores(self):
        global ID_PESSOA
        nome = self.nomePessoas.currentText()
        cpfCnpj = self.cpfCnpj.text()
        dataNascimento = self.dataDeNascimento.date()
        dataNascimento = self.retornaDate(dataNascimento)
        telefone = self.telefone.text()
        email = self.email.text()
        cargo = self.cargo.currentText()

        return (ID_PESSOA, nome, cpfCnpj, dataNascimento, telefone, email, cargo)

    def getKey(self):
        indice = self.nomePessoas.currentIndex()
        key = list(self.dicionarioPessoas.keys())
        return key[indice]
    
    def popularCampos(self):
        key = self.getKey()
        self.setIdPessoa(key)
        dados = buscarPessoaId(key)
        self.email.setText(dados.get('email'))
        self.cpfCnpj.setText(dados.get('cpfCnpj'))
        self.telefone.setText(dados.get('telefone'))
        self.cargo.setCurrentText(dados.get('cargo'))
        self.setDataNascimento(dados.get('dataNasc'))
    
    def setDataNascimento(self, data):
        data = data.__str__()
        data = data.split('-')
        objeto = QDate()
        objeto.setDate(int(data[0]), int(data[1]), int(data[2]))
        self.dataDeNascimento.setDate(objeto)

    def retornaDate(self, date):
        date = (str(date.year()), str(date.month()), str(date.day()))
        dataFinal = '-'.join(date)
        return dataFinal
    
    def setIdPessoa(self, id):
        global ID_PESSOA
        ID_PESSOA = id

    def setIndexInicial(self):
        self.nomePessoas.setCurrentIndex(0)
 