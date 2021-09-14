"""Add slack token field to organisation

Revision ID: 7bc746997e8d
Revises: 5c0498e264bc
Create Date: 2019-08-05 17:47:01.203644

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = "7bc746997e8d"
down_revision = "5c0498e264bc"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "organisation",
        sa.Column("chat_token_slack", sa.String(length=80), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("organisation", "chat_token_slack")
