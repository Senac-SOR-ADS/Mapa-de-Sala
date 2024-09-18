from conexao import ConexaoBD


class Login:
    def __init__(self, email, senha) -> None:
        self.__email = email
        self.__senha = senha
        self.__idLogin = None
        self.__idPessoa = None
        self.__banco = ConexaoBD()

    def get_idLogin(self):
        return self.__idLogin

    def set_idLogin(self, id):
        self.__idLogin = id
    
    def get_idPessoa(self):
        return self.__idPessoa

    def set_idPessoa(self):
        self.__idPessoa

    def getEmail(self):
        return self.__email

    def getSenha(self):
        return self.__senha

    def validarLogin(self):
        self.__banco.conectar()

        query = "SELECT * FROM login WHERE email = %s AND senha = %s;"
        parametros = (self.getEmail(), self.getSenha())
        resultado = self.__banco.buscar(query,  parametros)

        self.__banco.desconectar()

        try:
            if self.getEmail() == resultado[2] and self.getSenha() ==  resultado[3]:
                self.set_idLogin(resultado[0])
                print(f"id Login: {resultado[0]}")
                self.__idPessoa = resultado[1]
                print(f"id Pessoa: {resultado[1]}")
                return True
        except:
            return False

if __name__ == "__main__":
    login = Login(email='emailgenerico@gmail.com', senha='senha456')
    if login.validarLogin():
        print("validado!")
    else:
        print("erro")

    # print(type(login.validarLogin()))
