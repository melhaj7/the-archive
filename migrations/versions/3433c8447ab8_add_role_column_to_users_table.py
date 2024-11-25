"""add role column to users table

Revision ID: 3433c8447ab8
Revises: ef58bb564210
Create Date: 2024-11-20 13:55:15.254955

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3433c8447ab8'
down_revision = 'ef58bb564210'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', sa.String(length=50), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('role')

    # ### end Alembic commands ###
