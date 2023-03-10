"""add created_at to user

Revision ID: 853c5adc9aa3
Revises: 450c10f974e2
Create Date: 2023-02-14 17:43:32.003990

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '853c5adc9aa3'
down_revision = '450c10f974e2'
branch_labels = ()
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('created_at', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'created_at')
    # ### end Alembic commands ###
