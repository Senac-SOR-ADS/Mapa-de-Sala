from conexao import ConexaoBD


class Login:
    def __init__(self, pessoa, email, senha) -> None:
        self.__pessoa = pessoa
        self.email = email
        self.senha = senha
        self.__banco = ConexaoBD()
 
<<<<<<< Updated upstream
    def get_pessoa(self):
        return self.__pessoa
   
    def set_pessoa(self, pessoa):
        self.__pessoa = pessoa
=======
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
        return Pessoa.getIdPessoa()
    
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
    login.validarLogin()
        # print(login.get_idPessoa())
        # print('login com sucesso')
        # print(login.compararLogin())

    # print(type(login.validarLogin()))
>>>>>>> Stashed changes
