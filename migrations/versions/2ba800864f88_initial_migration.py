"""initial migration

Revision ID: 2ba800864f88
Revises: 
Create Date: 2021-10-20 16:30:09.244013

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ba800864f88'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('appointments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('phone_number', sa.String(length=50), nullable=False),
    sa.Column('provider_name', sa.String(length=50), nullable=False),
    sa.Column('delta', sa.Integer(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('timezone', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('appointments')
    # ### end Alembic commands ###