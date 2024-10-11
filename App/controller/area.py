from App.model.area import Area

def cadastroDeArea(nomeArea):
    areaModel = Area(nomeArea)
    if areaModel.cadastrar_area():
        return True
    return False

def listarAreas():
    todas_areas = Area('').consulta_nome_areas()
    lista = [ i[0] for i in todas_areas]
    return lista

