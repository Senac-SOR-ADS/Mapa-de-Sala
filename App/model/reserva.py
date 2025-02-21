

from App.model.conexao import ConexaoBD
from App.model.curso import Curso
from App.controller.logger import Log

log = Log('model')


class Reserva:
    __banco = ConexaoBD()
    
    def __init__(self, idLogin, idPessoa, idCurso, idSala, dia, horaInicio, horaFim, chaveDevolvida = 0, observacao = None):
        self.__idLogin = idLogin
        self.__idPessoa = idPessoa
        self.__idCurso = idCurso
        self.__idSala = idSala
        self.__dia = dia
        self.__horaInicio = horaInicio
        self.__horaFim = horaFim
        self.__chaveDevolvida = chaveDevolvida
        self.__observacao = observacao
        self.__id = None

    def __setIdReserva(self, id):
        self.__id = id

    def get_idReserva(self):
        return self.__id

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
        query = "INSERT INTO reserva (idLogin, idPessoa, idCurso, idSala, dia, hrInicio, hrFim, chaveDevolvida, observacao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        parametros = (self.__idLogin, self.__idPessoa, self.__idCurso, self.__idSala, self.__dia, self.__horaInicio, self.__horaFim, self.__chaveDevolvida ,self.__observacao)
        self.__banco.alterarDados(query, parametros)
        self.__banco.desconectar()
        return True
            
    @classmethod
    def validar_periodo(cls, idSala, dia, horaInicio, horaFim):
        """Verifica se já existe uma reserva na data que foi requisitada"""
        cls.__banco.conectar()
        query_verifica = "SELECT * FROM reserva WHERE idSala = %s AND dia = %s AND ((hrInicio < %s AND hrFim > %s) OR (hrInicio >= %s AND hrFim <= %s))"
        parametros_verifica = (idSala, dia, horaFim, horaInicio, horaInicio, horaFim)
        resultado = cls.__banco.buscarTodos(query_verifica, parametros_verifica)
        cls.__banco.desconectar()
        if resultado:
            return resultado
        log.info(f"{__name__}: Reserva já existe dentro das datas requisitadas.")
        return False
    
    @classmethod
    def validar_troca(cls, idSala, dia, hrInicio, hrFim):
        """Verifica se já existe uma reserva na data que foi requisitada"""
        cls.__banco.conectar()
        query_verifica = "SELECT * FROM reserva WHERE idSala = %s AND dia = %s AND ((hrInicio < %s AND hrFim > %s) OR (hrInicio >= %s AND hrFim <= %s))"
        parametros_verifica = (idSala, dia, hrFim, hrInicio, hrInicio, hrFim)
        resultado = cls.__banco.buscarTodos(query_verifica, parametros_verifica)
        cls.__banco.desconectar()
        if len(resultado) <= 1 :
            return True
        return False

    @classmethod
    def retornar_reserva(cls):
        """Uma função para devolver os dados da tabela de reserva do banco"""
        cls.__banco.conectar()
        query = "SELECT * FROM reserva"
        resultado = cls.__banco.buscarTodos(query)
        cls.__banco.desconectar()
        listaReserva = cls.getListaReserva(resultado)
        return listaReserva
    
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
    
    @classmethod
    def getListaReserva(cls, dados):
        listaReservas = list()
        for reserva in dados:
            objetoReserva = cls(reserva[1], reserva[2], reserva[3], reserva[4], reserva[5], reserva[6], reserva[7], reserva[8])
            objetoReserva.__setIdReserva(reserva[0])
            listaReservas.append(objetoReserva)
        return listaReservas
    
    @classmethod
    def deletar(cls, idReserva):
        cls.__banco.conectar()
        query = "DELETE FROM reserva WHERE idReserva = %s"
        parametro = [idReserva]
        resultado = cls.__banco.alterarDados(query, parametro)
        cls.__banco.desconectar()
        if resultado.rowcount:
            log.info(f"{__name__}: Reserva deletada com sucesso.")
            return True
        log.info(f"{__name__}: Reserva não foi deletada.")
        return False
    
    @classmethod
    def retorna_reservas_curso(cls, idCurso):
        cls.__banco.conectar()
        query = 'SELECT * FROM reserva WHERE idCurso = %s'
        resultado = cls.__banco.buscarTodos(query, [idCurso,])
        cls.__banco.desconectar()
        if resultado:
           return resultado
        return False
    
    @classmethod
    def retorna_reserva_by_periodo(cls, oferta, diaInicio, diaFim):
        idCurso = Curso.retorna_id_oferta(oferta)
        resultado = None
        if idCurso:
            cls.__banco.conectar()
            query = 'SELECT * FROM reserva WHERE dia >= %s and dia <= %s and idCurso = %s'
            params = [diaInicio, diaFim, idCurso]
            resultado = cls.__banco.buscarTodos(query, params)
            cls.__banco.desconectar()
        return resultado
    
    @classmethod
    def atualizar(cls, idLogin, idPessoa, idCurso, idSala, dia, hrInicio, hrFim, chaveDevolvida, observacao, idReserva):
        cls.__banco.conectar()
        query = "UPDATE reserva SET idLogin= %s, idPessoa= %s,idCurso= %s,idSala= %s,dia= %s,hrInicio= %s,hrFim= %s, chaveDevolvida= %s , observacao= %s WHERE idReserva = %s"
        parametro = [idLogin, idPessoa, idCurso, idSala, dia, hrInicio, hrFim, chaveDevolvida, observacao, idReserva]
        resultado = cls.__banco.alterarDados(query, parametro)
        cls.__banco.desconectar()
        if resultado.rowcount:
            return True
        log.error(f"{__name__}: Reserva não foi atualizada.")
        return False

    
    @classmethod
    def trocar_sala(cls, idLogin, idSala, dia, hrInicio, hrFim):
        cls.__banco.conectar()
        query = "UPDATE reserva SET idLogin = %s, idSala = %s, dia = %s, hrInicio = %s, hrFim = %s"
        parametro = [idLogin, idSala, dia, hrInicio, hrFim]
        resultado = cls.__banco.alterarDados(query, parametro)
        cls.__banco.desconectar()
        if resultado.rowcount:
            return True
        log.error(f"{__name__}: Salas não foram trocadas.")
        return False
        
    @classmethod
    def buscar_data(cls, diaInicio, diaFim):
        cls.__banco.conectar()
        query = "SELECT * FROM reserva WHERE dia >= %s AND dia <= %s ORDER BY dia DESC;"
        parametro = [diaInicio, diaFim]
        resultado = cls.__banco.buscarTodos(query, parametro)
        cls.__banco.desconectar()
        if resultado:
            listaReserva = cls.getListaReserva(resultado)
            return listaReserva
        log.error(f"{__name__}: Nenhuma reserva durante essas datas")

    @classmethod
    def buscar_data_oferta(cls, diaInicio, diaFim, idCurso):
        cls.__banco.conectar()
        query = "SELECT * FROM reserva WHERE dia >= %s AND dia <= %s AND idCurso = %s ORDER BY dia DESC;"
        parametro = [diaInicio, diaFim, idCurso]
        resultado = cls.__banco.buscarTodos(query, parametro)
        cls.__banco.desconectar()
        if resultado:
            listaReserva = cls.getListaReserva(resultado)
            return listaReserva
        log.error(f"{__name__}: Nenhuma reserva deste curso neste período")

    @classmethod
    def buscar_data_sala(cls, diaInicio, diaFim, idSala):
        cls.__banco.conectar()
        query = "SELECT * FROM reserva WHERE dia >= %s AND dia <= %s AND idSala = %s ORDER BY dia DESC;"
        parametro = [diaInicio, diaFim, idSala]
        resultado = cls.__banco.buscarTodos(query, parametro)
        cls.__banco.desconectar()
        if resultado:
            listaReserva = cls.getListaReserva(resultado)
            return listaReserva
        log.error(f"{__name__}: Nenhuma reserva nesta sala durante esse período")

    @classmethod
    def buscar_data_periodo(cls, diaInicio, diaFim, horaInicio, horaFim):
        cls.__banco.conectar()
        query = "SELECT * FROM reserva WHERE dia >= %s AND dia <= %s AND hrInicio >= %s AND hrFim <= %s ORDER BY dia DESC;"
        parametro = [diaInicio, diaFim, horaInicio, horaFim]
        resultado = cls.__banco.buscarTodos(query, parametro)
        cls.__banco.desconectar()
        if resultado:
            listaReserva = cls.getListaReserva(resultado)
            return listaReserva
        log.error(f"{__name__}: Nenhuma reserva neste horário durante esse período")

    @classmethod
    def buscar_data_periodo_oferta(cls, diaInicio, diaFim, horaInicio, horaFim, idCurso):
        cls.__banco.conectar()
        query = "SELECT * FROM reserva WHERE dia >= %s AND dia <= %s AND hrInicio >= %s AND hrFim <= %s AND idCurso = %s ORDER BY dia DESC;"
        parametro = [diaInicio, diaFim, horaInicio, horaFim, idCurso]
        resultado = cls.__banco.buscarTodos(query, parametro)
        cls.__banco.desconectar()
        if resultado:
            listaReserva = cls.getListaReserva(resultado)
            return listaReserva
        log.error(f"{__name__}: Nenhuma reserva deste curso, durante este horário")

    @classmethod
    def buscar_periodo_sala(cls, diaInicio, diaFim, horaInicio, horaFim, idSala):
        cls.__banco.conectar()
        query = "SELECT * FROM reserva WHERE dia >= %s AND dia <= %s AND hrInicio >= %s AND hrFim <= %s AND idSala = %s ORDER BY dia DESC;"
        parametro = [diaInicio, diaFim, horaInicio, horaFim, idSala]
        resultado = cls.__banco.buscarTodos(query, parametro)
        cls.__banco.desconectar()
        if resultado:
            listaReserva = cls.getListaReserva(resultado)
            return listaReserva
        log.error(f"{__name__}: Nenhuma reserva nesta sala durante este horário")

    @classmethod
    def buscar_oferta_sala(cls, diaInicio, diaFim, idCurso, idSala):
        cls.__banco.conectar()
        query = "SELECT * FROM reserva WHERE dia >= %s AND dia <= %s AND idSala = %s AND idCurso = %s ORDER BY dia DESC;"
        parametro = [diaInicio, diaFim, idSala, idCurso]
        resultado = cls.__banco.buscarTodos(query, parametro)
        cls.__banco.desconectar()
        if resultado:
            listaReserva = cls.getListaReserva(resultado)
            return listaReserva
        log.error(f"{__name__}: Nenhuma reserva deste curso nesta sala")

    @classmethod
    def buscar_periodo_sala_oferta(cls, diaInicio, diaFim, idSala, idCurso, horaInicio, horaFim):
        cls.__banco.conectar()
        query = "SELECT * FROM reserva WHERE dia >= %s AND dia <= %s AND idSala = %s AND idCurso = %s AND hrInicio >= %s AND hrFim <= %s ORDER BY dia DESC;"
        parametro = [diaInicio, diaFim, idSala, idCurso, horaInicio, horaFim]
        resultado = cls.__banco.buscarTodos(query, parametro)
        cls.__banco.desconectar()
        if resultado:
            listaReserva = cls.getListaReserva(resultado)
            return listaReserva
        log.error(f"{__name__}: Nenhuma reserva deste curso nesta sala durante esse horário")

if __name__ == "__main__":
    pass