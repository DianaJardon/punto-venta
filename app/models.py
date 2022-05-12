"""
    The following script contains the db models that interacts with the web-app
"""

# absolute imports
from flask_login import UserMixin, login_manager
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

    def __init__(self, user_name, last_name, user_email, password_hash) -> None:
        self.user_name = user_name
        self.last_name = last_name
        self.user_email = user_email
        self.password_hash = password_hash
        super().__init__()

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


