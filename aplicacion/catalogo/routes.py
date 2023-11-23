from . import catalogo
from flask import render_template


@catalogo.route('/catalogo')
def catalog():
    """Página de catálogo de productos"""
    return render_template('Catalogo.html')