class Curso:
    def __init__(self, idArea, nome, oferta, periodo, cargaHoraria, horasDia, qtdAlunos):
        self.__idArea = idArea
        self.__nome = nome
        self.__oferta = oferta
        self.__periodo = periodo
        self.__cargaHoraria = cargaHoraria
        self.__horasDia = horasDia
        self.__qtdAlunos = qtdAlunos
    
    def get_idArea(self):
        return self.__idArea
    
    def set_idArea(self, idArea):
        self.__idArea = idArea

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def get_oferta(self):
        return self.__oferta
    
    def set_oferta(self, oferta):
        self.__oferta = oferta

    def get_periodo(self):
        return self.__periodo
    
    def set_oferta(self, periodo):
        self.__periodo = periodo

    def get_cargaHoraia(self):
        return self.__cargaHoraria
    
    def set_cargaHoraria(self, cargaHoraria):
        self.__cargaHoraria = cargaHoraria

    def get_horasDia(self):
        return self.__horasDia
    
    def set_horasDia(self, horasDias):
        self.__horasDia = horasDias

    def get_qtdAlunos(self):
        return self.__qtdAlunos
    
    def set_qtdAlunos(self, qtdAlunos):
        self.__qtdAlunos = qtdAlunos