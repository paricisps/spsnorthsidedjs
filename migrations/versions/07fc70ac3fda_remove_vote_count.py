"""remove vote_count

Revision ID: 07fc70ac3fda
Revises: 5a19e557c33f
Create Date: 2023-08-14 10:43:59.812676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07fc70ac3fda'
down_revision = '5a19e557c33f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('voted_songs', schema=None) as batch_op:
        batch_op.drop_column('vote_count')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('voted_songs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('vote_count', sa.INTEGER(), nullable=True))

    # ### end Alembic commands ###
