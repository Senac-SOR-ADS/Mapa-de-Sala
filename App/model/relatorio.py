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
