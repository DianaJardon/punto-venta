from flask_login import login_required
from flask import render_template, request

#local imports
from . import inventory


@inventory.route('/home')

#decorator
@login_required
def home():

    return render_template('inventory/inventario_inicio.html')

@login_required
def pagos():
    pass