"""auto migrations

Revision ID: 575752db4068
Revises: 7058db7f1e6d
Create Date: 2023-09-07 12:50:22.365441

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '575752db4068'
down_revision: Union[str, None] = '7058db7f1e6d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
