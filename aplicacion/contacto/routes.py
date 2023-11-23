from flask import render_template
from . import contacto


@contacto.route('/contacto')
def contact():
    """Página de contacto"""
    return render_template('Contact.html')
