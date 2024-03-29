"""create classrooms table

Revision ID: 92239c616013
Revises: 622f47cd4d70
Create Date: 2024-03-14 14:32:43.646503

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '92239c616013'
down_revision: Union[str, None] = '622f47cd4d70'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    table = op.create_table(
        'classrooms',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.String(50)),
        sa.Column('monitor', sa.String(50)),
    )

    op.bulk_insert(
        table,
        [
            {'name': '43B', 'description': 'Classroom in block B', 'monitor': 'Juan Muñoz'},
            {'name': '51K', 'description': 'Classroom in block K', 'monitor': 'Alberto Linero'},
            {'name': '14F', 'description': 'Classroom in block F', 'monitor': 'Pedro Escalante'}
        ]
    )

def downgrade() -> None:
    op.drop_table('classrooms')
