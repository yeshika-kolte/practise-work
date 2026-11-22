"""table create

Revision ID: 1c01fc81a6e2
Revises: e9e7f7862df3
Create Date: 2026-07-06 12:05:37.860151

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1c01fc81a6e2'
down_revision: Union[str, Sequence[str], None] = 'e9e7f7862df3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
