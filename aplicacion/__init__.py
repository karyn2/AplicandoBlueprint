from flask import Flask
from .catalogo import catalogo
from .inicio import inicio
from .contacto import contacto

app = Flask(__name__)
app.config.from_pyfile('config/configuracion.cfg')
app.register_blueprint(catalogo)
app.register_blueprint(inicio)
app.register_blueprint(contacto)
