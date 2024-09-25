from conexao import ConexaoBD


class Reserva:
    def __init__(self, idLogin, idPessoa, idCurso, idSala, dia, horaInicio, horaFim, observacao = None):
        self.__idLogin = idLogin
        self.__idPessoa = idPessoa
        self.__idCurso = idCurso
        self.__idSala = idSala
        self.__dia = dia
        self.__horaInicio = horaInicio
        self.__horaFim = horaFim
        self.__observacao = observacao
        self.__banco = ConexaoBD()

    def get_idLogin(self):
        return self.__idLogin
    
    def set_idLogin(self, idLogin):
        self.__idLogin = idLogin

    def get_idPessoa(self):
        return self.__idPessoa
    
    def set_idPessoa(self, idPessoa):
        self.__idPessoa = idPessoa

    def get_idCurso(self):
        return self.__idCurso
    
    def set__idCurso(self, idCurso):
        self.__idCurso = idCurso

    def get_idSala(self):
        return self.__idSala
    
    def set_idSala(self, idSala):
        self.__idSala = idSala
    
    def get_dia(self):
        return self.__dia
    
    def set_dia(self, dia):
        self.__dia = dia 

    def get_horaInicio(self):
        return self.__horaInicio
    
    def set_horaInicio(self, horaInicio):
        self.__horaInicio = horaInicio

    def get_horaFim(self):
        return self.__horaFim
    
    def set_horaFim(self, horaFim):
        self.__horaFim = horaFim

    def fazer_reserva(self):
        """Uma função para você tentar fazer uma reserva, caso já exista uma reserva no mesmo horário, dia e sala, ele alerta você. Caso contrário ele faz a reserva"""
        self.__banco.conectar()
        query_verifica = "SELECT * FROM reserva WHERE idSala = %s AND dia = %s AND ((hrInicio < %s AND hrFim > %s) OR (hrInicio >= %s AND hrFim <= %s))"
        parametros_verifica = (self.__idSala, self.__dia, self.__horaFim, self.__horaInicio, self.__horaInicio, self.__horaFim)
        resultado = self.__banco.buscarTodos(query_verifica, parametros_verifica)
        if resultado != []:
            print("Dentro desse intervalo já existe uma reserva")
            return False
        else:
            query = "INSERT INTO reserva (idLogin, idPessoa, idCurso, idSala, dia, hrInicio, hrFim, observacao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            parametros = (self.__idLogin, self.__idPessoa, self.__idCurso, self.__idSala, self.__dia, self.__horaInicio, self.__horaFim, self.__observacao)
            self.__banco.alterarDados(query, parametros)
            self.__banco.desconectar()
            return True

    def retornar_reserva(self):
        """Uma função para devolver os dados da tabela de reserva do banco"""
        self.__banco.conectar()
        query = "SELECT * FROM reserva"
        resultado = self.__banco.buscarTodos(query)
        self.__banco.desconectar()
        return resultado
    
    def retornar_reserva_login(self):
        """Retorna as reservas de um dia, junto com o horário da reserva, o nome de quem fez a reserva e a observação da reserva"""
        self.__banco.conectar()
        query = "SELECT p.nome, r.hrInicio, r.hrFim, r.dia, r.observacao FROM reserva r JOIN login l ON r.idLogin = l.idLogin JOIN pessoa p ON l.idPessoa = p.idPessoa WHERE r.dia = %s; "
        parametro = ([self.__dia])
        resultado = self.__banco.buscarTodos(query, parametro)
        self.__banco.desconectar()
        return resultado

    def retorna_reserva_pessoa(self):
        """Retorna as reservas de um dia, junto do horário da reserva, nome da pessoa que vai usar a reserva e a observação da reserva"""
        self.__banco.conectar()
        query = "SELECT p.nome, r.hrInicio, r.hrFim, r.dia, r.observacao FROM reserva r JOIN pessoa p ON p.idPessoa = r.idPessoa WHERE r.dia = %s; "
        parametro = ([self.__dia])
        resultado = self.__banco.buscarTodos(query, parametro)
        self.__banco.desconectar()
        return resultado
    
    def retorna_reserva_sala(self):
        """Retorna o dia da reserva, junto do nome da sala, nome da pessoa que vai usar, horário da reserva, nome do curso e observação"""
        self.__banco.conectar()
        query = "SELECT r.dia, s.nome AS nomeSala, p.nome AS nomeDocente, r.hrInicio, r.hrFim, c.oferta AS curso, r.observacao FROM reserva r JOIN sala s ON r.idSala = s.idSala JOIN pessoa p ON r.idPessoa = p.idPessoa JOIN curso c ON r.idCurso = c.idCurso; "
        resultado = self.__banco.buscarTodos(query)
        self.__banco.desconectar()
        return resultado
    
    def retorna_reserva_dia(self):
        """Retorna as reservas de um dia, com o nome da pessoa que vai usar, horário da reserva, nome do curso e observação"""
        self.__banco.conectar()
        query = "SELECT p.nome, r.hrInicio, r.hrFim, r.dia, c.nome, r.observacao FROM reserva r JOIN pessoa p ON p.idPessoa = r.idPessoa JOIN curso c ON r.idCurso = c.idCurso WHERE r.dia = %s"
        parametro = ([self.__dia])
        resultado = self.__banco.buscarTodos(query, parametro)
        self.__banco.desconectar()
        return resultado

if __name__ == "__main__":
    pass