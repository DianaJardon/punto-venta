"""empty message

Revision ID: b77d8758a35b
Revises: 0129991cd2b2
Create Date: 2022-05-04 20:44:24.859644

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b77d8758a35b'
down_revision = '0129991cd2b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('user_name', sa.String(length=80), nullable=False))
    op.add_column('user', sa.Column('user_email', sa.String(length=120), nullable=False))
    op.drop_index('ix_user_email', table_name='user')
    op.drop_index('ix_user_name', table_name='user')
    op.create_index(op.f('ix_user_user_email'), 'user', ['user_email'], unique=False)
    op.create_index(op.f('ix_user_user_name'), 'user', ['user_name'], unique=False)
    op.drop_column('user', 'name')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('name', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_user_user_name'), table_name='user')
    op.drop_index(op.f('ix_user_user_email'), table_name='user')
    op.create_index('ix_user_name', 'user', ['name'], unique=False)
    op.create_index('ix_user_email', 'user', ['email'], unique=False)
    op.drop_column('user', 'user_email')
    op.drop_column('user', 'user_name')
    # ### end Alembic commands ###