"""
    The following script contains the db models that interacts with the web-app
"""

# absolute imports
from flask_login import UserMixin, login_manager
from sqlalchemy import ForeignKey
from werkzeug.security import check_password_hash, generate_password_hash

# relative imports
from app import db, login_manager


# Access models

class User(db.Model, UserMixin):
    __tablename__ = 'user_access'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_name = db.Column(db.String(80), index=True, nullable=False)
    last_name = db.Column(db.String(80), index=True)
    user_email = db.Column(db.String(120), index=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    @property
    def password(self):
        """
        prevenimos que la contraseña sea accedida desde otra instancia
        :return: Attribute Error
        """
        return AttributeError('No se puede acceder a la contraseña')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<Usuario: {self.user_name}'


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


# app interns model


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer(), autoincrement=True, nullable=False, primary_key=True)
    name = db.Column(db.String(120), index=True, nullable=False)
    description = db.Column(db.TEXT())
    product = db.relationship('Product', backref="product", lazy=True)


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer(), autoincrement=True, nullable=False, primary_key=True)
    category_id = db.Column(db.Integer(), ForeignKey('category.id'), nullable=False)
    name = db.Column(db.String(180), index=True, nullable=False)
    stock = db.Column(db.BIGINT(), index=True)
    price = db.Column(db.Float(), index=True)
