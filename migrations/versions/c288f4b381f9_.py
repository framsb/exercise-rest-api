"""empty message

Revision ID: c288f4b381f9
Revises: f722c379de27
Create Date: 2022-07-24 01:11:33.511368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c288f4b381f9'
down_revision = 'f722c379de27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(length=20), nullable=False))
    op.create_unique_constraint(None, 'user', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'username')
    # ### end Alembic commands ###
