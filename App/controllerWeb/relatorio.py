from datetime import datetime
from App.model.relatorio import Relatorio
from typing import List, Optional

def pesquisarDia(data: Optional[datetime.date] = None) -> List[dict]:
    data = data or datetime.date.today()
    reservas = Relatorio.buscar_reservas_por_dia(data) or []
    
    return [
        {
            'nomePessoa': reserva['nomePessoa'],
            'nomeCurso': reserva['nomeCurso'],
            'nomeSala': reserva['nomeSala'],
            'hora_inicio': reserva['horaInicio'],
            'hora_fim': reserva['horaFim'],
            'observacao': reserva['observacao']
        }
        for reserva in reservas
    ]