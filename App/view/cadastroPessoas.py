from PyQt5.QtWidgets import QWidget, QLineEdit, QComboBox, QDateEdit
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot, QDate
from App.controller.pessoa import cadastrarPessoa
from App.controller.utils import modificarData
from App.controller.utils import  validarInputs, sucessoCadastro, erroCadastro
from PyQt5.QtCore import QTimer

class cadastroPessoas(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/cadastroPessoas.ui',self)

        self.dataDeNascimento = self.findChild(QDateEdit, 'dataDeNascimento')

        self.dataDeNascimento.setCalendarPopup(True)
        self.dataDeNascimento.setDisplayFormat('dd/MM/yyyy')
        self.dataDeNascimento.setDate(QDate.currentDate()) 
    
    def getDadosCadastro(self):
        nomePessoas = self.nomePessoas.text().strip()
        cpfCnpj = self.cpfCnpj.text().strip()
        email = self.email.text().strip()
        dataDeNascimento = modificarData(self.dataDeNascimento.text().strip())
        cargo = self.cargo.currentText()
        telefone = self.telefone.text().strip()
        
        return (nomePessoas, cpfCnpj, dataDeNascimento, telefone, email, cargo)
        
    def limparCampos(self, *campos):
        for campo in campos:
            if isinstance(campo, QLineEdit):
                campo.clear()
            elif isinstance(campo, QComboBox):
                campo.setCurrentIndex(0)
            # elif isinstance(campo, QDateEdit):
            #     campo.setDate(QDateEdit.currentDate()) 


    @pyqtSlot()
    def on_btnCadastrar_clicked(self):
        campos = self.getDadosCadastro()
        if validarInputs(campos):
            cadastro = cadastrarPessoa(campos[0], campos[1], campos[2], campos[3], campos[4], campos[5])
            if cadastro == True:
                sucessoCadastro(self)
                self.setIndexInicial()
            else:
                erroCadastro(self)
        else:
            erroCadastro(self)

    def setIndexInicial(self):
        data = QDate.currentDate()
        self.nomePessoas.setText('')
        self.cpfCnpj.setText('')
        self.email.setText('')
        self.dataDeNascimento.setDate(data)
        self.cargo.setCurrentIndex(0)
        self.telefone.setText('')