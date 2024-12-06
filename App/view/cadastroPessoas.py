from PyQt5.QtWidgets import QWidget, QLineEdit, QComboBox, QDateEdit
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot, QDate
from App.controller.pessoa import cadastrarPessoa
from App.controller.utils import modificarData
from App.controller.utils import validarAcao
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
        dataDeNascimento = self.dataDeNascimento.text().strip()
        cargo = self.cargo.currentText()
        telefone = self.telefone.text().strip()

        dados = {"nome": nomePessoas,
                 "cpfCnpj": cpfCnpj,
                 "dataDeNascimento": modificarData(dataDeNascimento),
                 "telefone": telefone,
                 "email": email,
                 "cargo": cargo}
        return dados
        
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
        if cadastrarPessoa(*campos.values()):
            print('Pessoa cadastrada com sucesso!')
            validarAcao()
        else:
            print('Erro ao cadastrar pessoa!')
