from App.model.area import Area

def cadastroDeArea(nomeArea):
    areaModel = Area(nomeArea)
    if areaModel.cadastrar_area():
        return True
    return False