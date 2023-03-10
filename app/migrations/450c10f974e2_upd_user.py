"""upd user

Revision ID: 450c10f974e2
Revises: 944c3a3ce68c
Create Date: 2023-02-14 17:24:52.380776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '450c10f974e2'
down_revision = '944c3a3ce68c'
branch_labels = ()
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('name', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('password', sa.String(length=100), nullable=True))
    op.drop_index('ix_user_nickname', table_name='user')
    op.create_index(op.f('ix_user_name'), 'user', ['name'], unique=True)
    op.drop_column('user', 'nickname')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('nickname', sa.VARCHAR(length=64), nullable=True))
    op.drop_index(op.f('ix_user_name'), table_name='user')
    op.create_index('ix_user_nickname', 'user', ['nickname'], unique=False)
    op.drop_column('user', 'password')
    op.drop_column('user', 'name')
    # ### end Alembic commands ###
