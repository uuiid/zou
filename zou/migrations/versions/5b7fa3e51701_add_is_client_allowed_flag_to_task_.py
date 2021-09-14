"""Add is client allowed flag to task status

Revision ID: 5b7fa3e51701
Revises: 6d1b2c60f58b
Create Date: 2019-11-04 15:37:12.261423

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = "5b7fa3e51701"
down_revision = "6d1b2c60f58b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "task_status",
        sa.Column(
            "is_client_allowed", sa.Boolean(), nullable=True, default=False
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("task_status", "is_client_allowed")
    # ### end Alembic commands ###
