from flask import Flask
from App.routes.routes import routes

app = Flask(__name__)


app.register_blueprint(routes)

