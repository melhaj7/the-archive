"""add books table

Revision ID: a395de75a90b
Revises: 7fb4110fe7e3
Create Date: 2024-11-23 13:25:59.363854

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a395de75a90b'
down_revision = '7fb4110fe7e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('author', sa.String(length=120), nullable=False),
    sa.Column('publication_year', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_book_author'), ['author'], unique=False)
        batch_op.create_index(batch_op.f('ix_book_title'), ['title'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_book_title'))
        batch_op.drop_index(batch_op.f('ix_book_author'))

    op.drop_table('book')
    # ### end Alembic commands ###
