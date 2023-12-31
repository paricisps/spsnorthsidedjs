"""event users

Revision ID: 0afa529d1bcc
Revises: ae94382fedc1
Create Date: 2023-08-11 17:13:56.825725

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0afa529d1bcc'
down_revision = 'ae94382fedc1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event_users',
    sa.Column('event_user_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.event_id'], name='event_users_event_id'),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], name='event_users_user_id'),
    sa.PrimaryKeyConstraint('event_user_id'),
    sa.UniqueConstraint('event_user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('event_users')
    # ### end Alembic commands ###
