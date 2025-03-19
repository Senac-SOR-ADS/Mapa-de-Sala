from App.model.conexao import ConexaoBD
 
class Relatorio:
    __banco = ConexaoBD()
 
    @classmethod
    def relatorioDia(cls, dia):
       cls.__banco.conectar()
       query = '''SELECT s.nome AS nome_sala, r.hrInicio, r.hrFim, c.oferta, c.nome AS nome_curso, p.nome AS nome_docente FROM reserva r JOIN sala s ON r.idSala = s.idSala JOIN curso c ON r.idCurso = c.idCurso JOIN pessoa p ON r.idPessoa = p.idPessoa WHERE r.dia = %s;'''
       params = [dia]
       resultado = cls.__banco.buscarTodos(query, params)
       cls.__banco.desconectar()
       return resultado
    
    @classmethod
    def relatorioSala(cls, diaInicio, diaFim, idSala):
        cls.__banco.conectar()
        query = '''SELECT r.dia, c.oferta AS oferta, c.nome AS nomeCurso, s.nome AS nomeSala, p.nome AS docente, r.hrInicio, r.hrFim FROM reserva r JOIN curso c ON c.idCurso = r.idCurso JOIN sala s ON s.idSala = r.idSala JOIN pessoa p ON p.idPessoa = r.idPessoa WHERE r.dia BETWEEN %s AND %s AND r.idSala = %s ORDER BY r.dia'''
        params = [diaInicio, diaFim, idSala]
        resultado = cls.__banco.buscarTodos(query, params)
        cls.__banco.desconectar()
        return resultado
    
    @classmethod
    def relatorioSalaLivre(cls, dia, horaInicio, horaFim ):
        cls.__banco.conectar()
        query = '''SELECT DISTINCT s.nome, s.tipo, s.predio FROM sala s JOIN reserva r ON r.idSala != s.idSala WHERE r.dia = %s AND r.hrInicio BETWEEN %s AND %s AND r.hrFim BETWEEN %s AND %s'''
        params = [dia, horaInicio, horaFim, horaInicio, horaFim]
        resultado = cls.__banco.buscarTodos(query, params)
        cls.__banco.desconectar()
        return resultado
    
    @classmethod
    def relatorioDocente(cls, diaInicio, diaFim, idPessoa):
        cls.__banco.conectar()
        query = '''SELECT p.nome AS docente, r.dia, r.hrInicio, c.oferta AS oferta, c.nome AS nomeCurso, s.nome AS nomeSala FROM reserva r JOIN curso c ON c.idCurso = r.idCurso JOIN sala s ON s.idSala = r.idSala JOIN pessoa p ON p.idPessoa = r.idPessoa WHERE r.dia BETWEEN %s AND %s AND r.idPessoa = %s ORDER BY r.dia;'''
        params = [diaInicio, diaFim, idPessoa]
        resultado = cls.__banco.buscarTodos(query, params)
        cls.__banco.desconectar()
        return resultado
    
    @classmethod
    def buscar_reservas_por_dia(cls, dia):
        cls.__banco.conectar()

        query = """SELECT p.nome AS nomePessoa, c.nome AS nomeCurso, s.nome AS nomeSala, r.hrInicio, r.hrFim, r.observacao
                    FROM reserva r
                    JOIN pessoa p ON r.idPessoa = p.idPessoa
                    JOIN curso c ON r.idCurso = c.idCurso
                    JOIN sala s ON r.idSala = s.idSala
                    WHERE DATE(r.dia) = %s
                    ORDER BY r.hrInicio"""

        resultados = cls.__banco.buscarTodos(query, (dia,))
        reservas = [
            {
                "nomePessoa": res[0],
                "nomeCurso": res[1],
                "nomeSala": res[2],
                "horaInicio": res[3],
                "horaFim": res[4],
                "observacao": res[5]
            }
            for res in resultados
        ]
        cls.__banco.desconectar()
        return reservas

    @classmethod
    def relatorioCursosFinalizando(cls, diaInicio, diaFim):
        cls.__banco.conectar()
        query = '''WITH CursoReservas AS (SELECT r.idcurso, MIN(r.dia) AS diaInicioCurso FROM  reserva r GROUP BY r.idcurso), UltimaReservaPeriodo AS (SELECT r.idcurso, MAX(r.dia) AS diaFimCurso FROM reserva r WHERE r.dia BETWEEN %s AND %s GROUP BY r.idcurso) SELECT c.nome AS nomeCurso, cr.diaInicioCurso, urp.diaFimCurso, r.hrInicio, r.hrFim FROM CursoReservas cr JOIN UltimaReservaPeriodo urp ON cr.idcurso = urp.idcurso JOIN curso c ON cr.idcurso = c.idcurso JOIN  reserva r ON urp.idcurso = r.idcurso AND r.dia = urp.diaFimCurso'''
        params = [diaInicio, diaFim]
        resultado = cls.__banco.buscarTodos(query, params)
        cls.__banco.desconectar()
        return resultado