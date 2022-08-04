"""empty message

Revision ID: 1f1982bfcfe8
Revises: d5b315b50c7c
Create Date: 2022-08-02 21:10:54.835117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f1982bfcfe8'
down_revision = 'd5b315b50c7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('country',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=84), nullable=False),
    sa.Column('language', sa.String(length=84), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('states',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('country_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=84), nullable=False),
    sa.Column('initials', sa.String(length=2), nullable=False),
    sa.ForeignKeyConstraint(['country_id'], ['country.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cities',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('state_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=84), nullable=False),
    sa.ForeignKeyConstraint(['state_id'], ['states.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cities')
    op.drop_table('states')
    op.drop_table('country')
    # ### end Alembic commands ###