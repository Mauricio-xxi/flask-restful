"""add blacklist table

Revision ID: 024b52706e56
Revises: 651759e10722
Create Date: 2019-11-24 18:51:22.659735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '024b52706e56'
down_revision = '651759e10722'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_tokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blacklist_tokens')
    # ### end Alembic commands ###
