"""added the vote count in again

Revision ID: b8444680d57b
Revises: 078ea60f75c1
Create Date: 2023-08-14 14:46:45.930208

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8444680d57b'
down_revision = '078ea60f75c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('voted_songs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('vote_count', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('voted_songs', schema=None) as batch_op:
        batch_op.drop_column('vote_count')

    # ### end Alembic commands ###