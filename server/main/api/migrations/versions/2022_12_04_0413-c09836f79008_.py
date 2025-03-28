"""empty message

Revision ID: c09836f79008
Revises: 6dc11c45d2d4
Create Date: 2022-12-04 04:13:41.900961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c09836f79008'
down_revision = '6dc11c45d2d4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('atmospheric_pressure',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('pressure', sa.Integer(), nullable=True),
    sa.Column('altitude', sa.Integer(), nullable=True),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.Column('updatedAt', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('test_user_table', sa.Column('name', sa.String(length=30), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('test_user_table', 'name')
    op.drop_table('atmospheric_pressure')
    # ### end Alembic commands ###
