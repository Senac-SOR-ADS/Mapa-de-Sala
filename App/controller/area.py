from App.model.area import Area

def cadastroDeArea(nomeArea):
    areaModel = Area(nomeArea)
    if areaModel.cadastrar_area():
        return True
    return False

def listarAreas() -> dict:
    todas_areas = Area.consulta_areas()
    listaNome = {i[1]:i[0] for i in todas_areas}
    return listaNome

