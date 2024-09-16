from conexao import ConexaoBD
from pessoa import Pessoa

class Login(Pessoa):
    def __init__(self, email, senha, idLogin=None, idPessoa=None):
        self.__idLogin = idLogin
        self.__idPessoa = idPessoa
        self.__email = email
        self.__senha = senha
        self.__banco = ConexaoBD()
 
    def validarLogin(self):
        self.__banco.conectar()
        busca = self.__banco.buscar("SELECT * FROM login WHERE email = %s AND senha = %s;", (self.getEmail(), self.getSenha()) )
        self.__banco.desconectar()

        try:
            if self.getEmail() == busca[2] and self.getSenha() ==  busca[3]:
                self.__idLogin = busca[0]
                self.__idPessoa = busca[1]
                return True
        except:
            return False
    
    def get_idLogin(self):
        return self.__idLogin
    
    def get_idPessoa(self):
        return self.__idPessoa
    
    def getEmail(self):
        return self.__email
    
    def getSenha(self):
        return self.__senha
    
    def compararLogin(self):
        self.__banco.conectar()
        query = 'SELECT * FROM pessoas WHERE idPessoa = %s'
        self.__banco.buscar(query, (self.get_idPessoa(), ))



if __name__ == "__main__":
    login = Login(email='emailgenerico@gmail.com', senha='senha456')
    if login.validarLogin():
        print(login.get_idPessoa())
        print('login com sucesso')
        print(login.compararLogin())

    # print(type(login.validarLogin()))