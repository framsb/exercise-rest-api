"""empty message

Revision ID: 4490695e71b9
Revises: c4a1e4abfa21
Create Date: 2022-07-23 00:10:28.267160

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4490695e71b9'
down_revision = 'c4a1e4abfa21'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('planets', 'terrain')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planets', sa.Column('terrain', mysql.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
