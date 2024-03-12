"""create students table

Revision ID: 72dab7533de2
Revises: 
Create Date: 2024-03-06 19:08:13.733563

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '72dab7533de2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'students',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('last_name', sa.String(50), nullable=False),
        sa.Column('birth_date', sa.Date, nullable=False),
        sa.Column('id_number', sa.String(50), nullable=False),
        sa.Column('phone', sa.String(15), nullable=False)
    )

def downgrade() -> None:
    op.drop_table('students')