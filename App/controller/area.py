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

def atualizarArea(idArea, nome):
    if Area.atualizar(idArea, nome):
        return True
    return False
 
def deletarArea(idArea):
    if Area.deletar(idArea):
        return True
    return False
