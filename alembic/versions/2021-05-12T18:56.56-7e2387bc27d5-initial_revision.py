"""initial revision

Revision ID: 7e2387bc27d5
Revises: 
Create Date: 2021-05-12 18:56:56.763609

"""

import sqlalchemy as sa
from alembic import op

import db

# revision identifiers, used by Alembic.
revision = '7e2387bc27d5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('devices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('connection_params', db.helpers.encrypted_json.encrypted_json.EncryptedJSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=128), nullable=False),
    sa.Column('password', sa.LargeBinary(length=128), nullable=False),
    sa.Column('role', db.helpers.user_role.UserRole(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_login'), 'users', ['login'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_login'), table_name='users')
    op.drop_table('users')
    op.drop_table('devices')
    # ### end Alembic commands ###
