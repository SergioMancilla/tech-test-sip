"""create students table

Revision ID: 3c9e699e4b6a
Revises: 92239c616013
Create Date: 2024-03-14 14:32:52.297478

"""
import random

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3c9e699e4b6a'
down_revision: Union[str, None] = '92239c616013'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    classroom_ids = [1, 2, 3]

    table = op.create_table(
        'students',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('last_name', sa.String(50), nullable=False),
        sa.Column('birth_date', sa.Date, nullable=False),
        sa.Column('id_number', sa.String(50), nullable=False),
        sa.Column('phone', sa.String(15), nullable=False),
        sa.Column('classroom_id', sa.Integer, sa.ForeignKey('classrooms.id'), nullable=True)
    )

    op.bulk_insert(
        table,
        [
            { "name": "Lamar", "last_name": "Guy", "birth_date": "1997-08-16", "id_number": "8718525661", "phone": "(556) 387-2218", "classroom_id": random.choice(classroom_ids) },
            { "name": "Selma", "last_name": "Hatfield", "birth_date": "1999-02-15", "id_number": "2730236147", "phone": "(139) 886-7011", "classroom_id": random.choice(classroom_ids) },
            { "name": "Demetrius", "last_name": "Webb", "birth_date": "1999-03-09", "id_number": "0377734182", "phone": "1-452-361-6527", "classroom_id": random.choice(classroom_ids) },
            { "name": "Quail", "last_name": "Cleveland", "birth_date": "1997-08-16", "id_number": "2745154669", "phone": "1-624-816-0821", "classroom_id": random.choice(classroom_ids) },
            { "name": "Jackson", "last_name": "Cannon", "birth_date": "2000-07-11", "id_number": "8277684420", "phone": "1-787-601-6962", "classroom_id": random.choice(classroom_ids) },
            { "name": "Alexander", "last_name": "Garcia", "birth_date": "2002-12-30", "id_number": "9523803284", "phone": "1-733-388-5779", "classroom_id": random.choice(classroom_ids) },
            { "name": "Mikayla", "last_name": "Pacheco", "birth_date": "1999-02-06", "id_number": "3797374431", "phone": "(418) 523-5630", "classroom_id": random.choice(classroom_ids) },
            { "name": "Adria", "last_name": "Mcclure", "birth_date": "2001-08-12", "id_number": "1732717832", "phone": "(864) 255-7683", "classroom_id": random.choice(classroom_ids) },
            { "name": "Elijah", "last_name": "English", "birth_date": "1999-08-01", "id_number": "5173581252", "phone": "(663) 976-8588", "classroom_id": random.choice(classroom_ids) },
            { "name": "Ivana", "last_name": "Bender", "birth_date": "1998-03-13", "id_number": "4260456684", "phone": "1-486-654-3639", "classroom_id": random.choice(classroom_ids) },
            { "name": "Ryan", "last_name": "Shepard", "birth_date": "1997-11-14", "id_number": "9965317855", "phone": "(682) 422-1592", "classroom_id": random.choice(classroom_ids) },
            { "name": "Joel", "last_name": "Harrington", "birth_date": "2001-08-30", "id_number": "1855755959", "phone": "1-562-273-6152", "classroom_id": random.choice(classroom_ids) },
            { "name": "Alika", "last_name": "Reyes", "birth_date": "1997-11-23", "id_number": "7263678657", "phone": "1-619-966-7283", "classroom_id": random.choice(classroom_ids) },
            { "name": "Leonard", "last_name": "Robertson", "birth_date": "2000-01-17", "id_number": "5182748406", "phone": "1-637-177-3248", "classroom_id": random.choice(classroom_ids) },
            { "name": "Dustin", "last_name": "Riddle", "birth_date": "1998-12-11", "id_number": "6625753325", "phone": "1-668-326-6513", "classroom_id": random.choice(classroom_ids) },
            { "name": "Carson", "last_name": "Schmidt", "birth_date": "1998-10-18", "id_number": "1267768637", "phone": "(523) 458-0155", "classroom_id": random.choice(classroom_ids) },
            { "name": "Yeo", "last_name": "English", "birth_date": "2002-11-18", "id_number": "2416403558", "phone": "1-475-528-7353", "classroom_id": random.choice(classroom_ids) },
            { "name": "Guinevere", "last_name": "Golden", "birth_date": "1998-12-20", "id_number": "2551833889", "phone": "1-677-443-3131", "classroom_id": random.choice(classroom_ids) },
            { "name": "Kirestin", "last_name": "Buchanan", "birth_date": "2001-11-04", "id_number": "4894441072", "phone": "1-339-283-6421", "classroom_id": random.choice(classroom_ids) },
            { "name": "Dalton", "last_name": "Barnett", "birth_date": "2000-01-26", "id_number": "5222431071", "phone": "1-631-438-3258", "classroom_id": random.choice(classroom_ids)  }
        ]
    )

def downgrade() -> None:
    op.drop_table('students')