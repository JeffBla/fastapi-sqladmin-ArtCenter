"""Create User table

Revision ID: 6512332f4480
Revises: 
Create Date: 2024-09-29 15:56:45.204272

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '6512332f4480'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user', sa.Column('id', sa.Integer(), nullable=False,
                          primary_key=True),
        sa.Column('Name', sa.String(length=255), nullable=False),
        sa.Column('StudentID',
                  sa.String(length=255),
                  nullable=False,
                  unique=True),
        sa.Column('Password', sa.String(length=255), nullable=False),
        sa.Column('is_admin', sa.Boolean(), nullable=False))
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    op.drop_table('user')
    pass
    # ### end Alembic commands ###
