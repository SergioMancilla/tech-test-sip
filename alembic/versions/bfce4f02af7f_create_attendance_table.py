"""create attendance table

Revision ID: bfce4f02af7f
Revises: 3c9e699e4b6a
Create Date: 2024-03-14 14:34:58.127969

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bfce4f02af7f'
down_revision: Union[str, None] = '3c9e699e4b6a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'attendance',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), nullable=True),
        sa.Column('subject_id', sa.Integer, sa.ForeignKey('subjects.id'), nullable=True),
        sa.Column('attended', sa.Boolean, nullable=False),
    )

def downgrade() -> None:
    op.drop_table('attendance')