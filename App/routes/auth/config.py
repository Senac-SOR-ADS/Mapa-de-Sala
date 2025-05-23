from datetime import timedelta
import os

class Config:
    # Chave secreta usada para proteger sessões e cookies
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY') or os.urandom(24)

    # Define a duração da sessão permanente (minutos)
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=10)

    # Atualiza a sessão em cada requisição
    SESSION_REFRESH_EACH_REQUEST = True

    # Define o modo de debug (usando variável de ambiente ou valor padrão)
    DEBUG = os.getenv("DEBUG", "False") == "True"

