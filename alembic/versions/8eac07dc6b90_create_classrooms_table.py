"""create classrooms  table

Revision ID: 8eac07dc6b90
Revises: 8abdd8ecb2c8
Create Date: 2024-03-06 19:08:33.610153

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8eac07dc6b90'
down_revision: Union[str, None] = '8abdd8ecb2c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'classrooms',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.String(50)),
        sa.Column('monitor', sa.String(50)),
    )

def downgrade() -> None:
    op.drop_table('classrooms')