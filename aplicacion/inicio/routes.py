from flask import render_template
from . import inicio


@inicio.route('/')
def index():
    """Página Inicio"""
    return render_template('Index.html')
