from model.area import Area
from view.cadastrarArea import CadastrarArea

class AreaController(CadastrarArea):
    def __init__(self):
        super().__init__()
        self.show()
        
        self.btnCadastrarArea.clicked.connect(self.cadastroDeArea)
        
    def cadastroDeArea(self):
        nomeArea = self.getCadastroArea()
        areaModel = Area(nomeArea)
        if not nomeArea:
            return False
        else:
            areaModel.cadastrar_area()
            return True