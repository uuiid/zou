"""add is_for_all flage to playlists

Revision ID: 6aa446ee4072
Revises: 7417c8eb70d8
Create Date: 2020-04-02 16:48:05.015267

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '6aa446ee4072'
down_revision = '7417c8eb70d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('playlist', sa.Column('is_for_all', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('playlist', 'is_for_all')
    # ### end Alembic commands ###
