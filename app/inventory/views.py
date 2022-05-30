from flask import render_template
from flask_login import login_required

# local imports
from . import inventory
from ..models import Product


@inventory.route('/home')
# decorator
@login_required
def home():
    products = Product.query.filter().all()

    return render_template('inventory/inventario_inicio.html', products=products)


@login_required
def pagos():
    pass
