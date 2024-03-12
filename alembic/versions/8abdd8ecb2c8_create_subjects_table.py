"""create subjects  table

Revision ID: 8abdd8ecb2c8
Revises: 72dab7533de2
Create Date: 2024-03-06 19:08:20.973966

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8abdd8ecb2c8'
down_revision: Union[str, None] = '72dab7533de2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'subjects',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.String(50)),
    )

def downgrade() -> None:
    op.drop_table('subjects')