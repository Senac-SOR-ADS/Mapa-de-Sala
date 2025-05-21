from jinja2 import Environment, FileSystemLoader
import datetime
from typing import List, Optional
from App.model.relatorio import Relatorio
import webbrowser
from os.path import abspath, join
from App.controller.utils import modificarData

def gerarRelatorio(data: Optional[datetime.date] = None) -> List[dict]:
    # Definindo a data para hoje se não for especificada
    data = data or datetime.date.today()
    
    # Buscando as reservas para o dia especificado
    reservas = Relatorio.buscar_reservas_por_dia(data) or []
    if not isinstance(data, str):
        data = data.strftime('%d/%m/%Y')
    # Renderizando o template com as reservas
    diretorio = join(abspath(__file__), '../../view/relatorio')
    env = Environment(loader=FileSystemLoader(diretorio))

    template = env.get_template("listarDia.html")
    relatorio = template.render(reservas=reservas, data=data)

    resultado = join(diretorio, 'output.html')
    with open(resultado, 'w', encoding='utf-8') as f:
        f.write(relatorio)
    webbrowser.open(resultado)

def relatorioSalaLivre(dia=None, horaInicio='13:30', horaFim='17:30'):
    dia = dia or datetime.date.today().__str__()
    dados = Relatorio.relatorioSalaLivre(dia, horaInicio, horaFim) or []
    # Renderizando o template com as reservas
    diretorio = join(abspath(__file__), '../../view/relatorio')
    env = Environment(loader=FileSystemLoader(diretorio))
    template = env.get_template("listarSalaLivre.html")
    relatorio = template.render(dados=dados, data=dia, horas=[horaInicio, horaFim ])
    resultado = join(diretorio, 'output-salalivre.html')
    with open(resultado, 'w', encoding='utf-8') as f:
        f.write(relatorio)
    webbrowser.open(resultado)
