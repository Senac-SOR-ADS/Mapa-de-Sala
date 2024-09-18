from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QTimer
import subprocess
import sys
import os

class interfaceLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        try:
            loadUi('interfaceLogin.ui', self)  # Carregar o arquivo de interface UI
            
            # Remove a barra de título e as bordas da janela
            self.setWindowFlags(Qt.FramelessWindowHint)
            # Define a janela como transparente
            self.setAttribute(Qt.WA_TranslucentBackground)
            
            # Verifica se os widgets foram carregados corretamente
            self.check_widgets()
            
            # Conectando o botão de login à função getEmailSenha
            self.btnEntrar.clicked.connect(self.getEmailSenha)
        except Exception as e:
            print(f"Erro ao carregar a interface: {e}")
            sys.exit(1)  # Sai se houver um erro

    def check_widgets(self):
        # Verifica se os widgets necessários existem
        if not hasattr(self, 'btnEntrar'):
            raise AttributeError("O botão 'btnEntrar' não foi encontrado no arquivo UI.")
        if not hasattr(self, 'inputEmail'):
            raise AttributeError("O campo 'inputEmail' não foi encontrado no arquivo UI.")
        if not hasattr(self, 'inputSenha'):
            raise AttributeError("O campo 'inputSenha' não foi encontrado no arquivo UI.")

    def getEmailSenha(self):
        email = self.inputEmail.text()
        senha = self.inputSenha.text()

        if email and senha:
            print(f"Email: {email}, Senha: {senha}")  # Imprime os dados no console
            QTimer.singleShot(1000, self.redirecionarHome)  # Redireciona para a Home após 1 segundo
        else:
            QMessageBox.warning(self, "Aviso", "Dados incompletos")
            QTimer.singleShot(2000, lambda: self.limparCampos(self.inputEmail))  # Limpa após 2 segundos
            QTimer.singleShot(2000, lambda: self.limparCampos(self.inputSenha))  # Limpa após 2 segundos

    def redirecionarHome(self):
        # Obtém o caminho absoluto para o arquivo main.py na mesma pasta do script de login
        script_dir = os.path.dirname(os.path.abspath(__file__))
        main_path = os.path.join(script_dir, 'modelo2\main.py')
        
        # Executa o arquivo main.py
        subprocess.Popen(['python', main_path])
        self.close()  # Fecha a janela atual de login

    def limparCampos(self, campo):
        campo.clear()

if __name__ == "__main__":
    app = QApplication([])
    widget = interfaceLogin()
    widget.show()
    app.exec_()
