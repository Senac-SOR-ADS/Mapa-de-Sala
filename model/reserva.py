from conexao import ConexaoBD


class Reserva:
    def __init__(self, idEquipamentos, idLogin, idPessoa, idCurso, idSala, dia, horaInicio, horaFim, observacao):
        self.__idEquipametos = idEquipamentos
        self.__idLogin = idLogin
        self.__idPessoa = idPessoa
        self.__idCurso = idCurso
        self.__idSala = idSala
        self.__dia = dia
        self.__horaInicio = horaInicio
        self.__horaFim = horaFim
        self.observacao = observacao 
        self.__banco = ConexaoBD
    
    def get_idEquipamentos(self):
        return self.__idEquipametos
    
    def set_idEquipamentos(self, idEquipamentos):
        self.__idEquipametos = idEquipamentos

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