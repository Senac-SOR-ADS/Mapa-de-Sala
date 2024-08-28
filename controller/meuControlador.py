from model.meuModelo import meuModelo
from view.minhaView import minhaVisao
 
class MeuControlador:
    def __init__(self):
        self.modelo = meuModelo()
        self.visao = minhaVisao()
 
    def atualizar_dado(self):
        novoDado = self.visao.solicitarDado()
        self.modelo.atualizarDado(novoDado)
        self.visao.mostrarDado(self.modelo.obterDado())