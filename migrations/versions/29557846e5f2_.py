"""empty message

Revision ID: 29557846e5f2
Revises: 34c254b3d686
Create Date: 2022-07-12 01:09:58.832595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29557846e5f2'
down_revision = '34c254b3d686'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.Column('lastname', sa.String(length=60), nullable=False),
    sa.Column('gender', sa.String(length=60), nullable=False),
    sa.Column('eyes', sa.String(length=60), nullable=False),
    sa.Column('hair', sa.String(length=60), nullable=False),
    sa.Column('birth_year', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.Column('location', sa.String(length=60), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('climate', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite_character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.Column('characterid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['characterid'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['userid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite_character')
    op.drop_table('planets')
    op.drop_table('characters')
    # ### end Alembic commands ###