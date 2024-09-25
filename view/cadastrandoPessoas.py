from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QTimer, pyqtSlot



class cadastrandoPessoas(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('view/ui/cadastroPessoas.ui',self)
    
    @pyqtSlot()
    def on_btnCadastrar_clicked(self):
        return self.getDadosCadastro()
    
    def getDadosCadastro(self):
        nomePessoas = self.nomePessoas.text().strip()
        cpfCnpj = self.cpfCnpj.text().strip()
        email = self.email.text().strip()
        dataDeNascimento = self.dataDeNascimento.text().strip()
        cargo = self.cargo.text().strip()
        telefone = self.telefone.text().strip()

        dados = {"nome":nomePessoas,
                 "cpfCnpj":cpfCnpj,
                 "email":email,
                 "dataDeNascimento":dataDeNascimento,
                 "cargo":cargo,
                 "telefone":telefone}
        return dados
        
    def validandoDados(self):
        self.respostaCadastro.setText('Cadastro realizado.')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.respostaCadastro))

    def dadosInvalidos(self):
        self.respostaCadastro.setText('Dados incomoletos.')
        QTimer.singleShot(2000, lambda: self.limparCampos(self.respostaCadastro))

    def limparCampos(self, campo):
        campo.clear()

if __name__ == "__main__":
    app = QApplication([])
    widget = cadastrandoPessoas()
    widget.show()
    app.exec_()


