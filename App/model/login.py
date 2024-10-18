from App.model.conexao import ConexaoBD
from App.model.criptografia import Criptografia
 
 
class Login:
    def __init__(self, email, senha) -> None:
        self.__email = email
        self.__senha = senha
        self.__idLogin = None
        self.__idPessoa = None
        self.__banco = ConexaoBD()
 
    def getIdLogin(self):
        return self.__idLogin
 
    def setIdLogin(self, id):
        self.__idLogin = id
    def getIdPessoa(self):
        return self.__idPessoa
 
    def setIdPessoa(self, id):
        self.__idPessoa = id
 
    def getEmail(self):
        return self.__email
   
    def getSenha(self):
        return self.__senha
 
    def validarLogin(self):
        self.__banco.conectar()
 
        query = "SELECT * FROM login WHERE email = %s;"
        parametro = [self.getEmail()]
        resultado = self.__banco.buscar(query,  parametro)
 
        self.__banco.desconectar()
 
        try:
            senhaBanco = resultado[3]
            senhaBanco = senhaBanco.encode('utf-8')
            senhaUsuario = self.getSenha()
 
            if self.getEmail() == resultado[2] and Criptografia.validarSenha(senhaUsuario, senhaBanco):
                self.setIdLogin(resultado[0])
                self.setIdPessoa(resultado[1])
                return True
        except:
            return False
        
    def fazerLogin(self):
        self.__banco.conectar()
        query = "INSERT INTO `login`(`idPessoa`, `email`, `senha`) VALUES (%s, %s, %s)"
        params = (self.getIdPessoa, self.getEmail, self.getSenha)
        resultado = self.__banco.alterarDados(query, params)
        return resultado
 
if __name__ == "__main__":
    pass