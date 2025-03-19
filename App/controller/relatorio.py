from jinja2 import Environment, FileSystemLoader
import datetime
from typing import List, Optional
from App.model.relatorio import Relatorio

# from App.model.reserva import buscar_reservas_por_dia
import webbrowser
from os.path import abspath, join

def gerarRelatorio(data: Optional[datetime.date] = None) -> List[dict]:
    # Definindo a data para hoje se não for especificada
    data = data or datetime.date.today()
    
    # Buscando as reservas para o dia especificado
    reservas = Relatorio.buscar_reservas_por_dia(data) or []
    
    # Renderizando o template com as reservas
    diretorio = join(abspath(__file__), '../../view/relatorio')
    env = Environment(loader=FileSystemLoader(diretorio))

    template = env.get_template("listarDia.html")
    relatorio = template.render(reservas=reservas, data=data)

    resultado = join(diretorio, 'output.html')
    with open(resultado, 'w', encoding='utf-8') as f:
        f.write(relatorio)
    webbrowser.open(resultado)