"""create students table

Revision ID: 3c9e699e4b6a
Revises: 92239c616013
Create Date: 2024-03-14 14:32:52.297478

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3c9e699e4b6a'
down_revision: Union[str, None] = '92239c616013'
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
        sa.Column('phone', sa.String(15), nullable=False),
        sa.Column('classroom_id', sa.Integer, sa.ForeignKey('classrooms.id'), nullable=True)
    )

def downgrade() -> None:
    op.drop_table('students')