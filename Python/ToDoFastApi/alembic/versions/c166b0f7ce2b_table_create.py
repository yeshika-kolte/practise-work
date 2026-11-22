"""table create

Revision ID: c166b0f7ce2b
Revises: 1c01fc81a6e2
Create Date: 2026-07-06 12:08:29.934315

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c166b0f7ce2b'
down_revision: Union[str, Sequence[str], None] = '1c01fc81a6e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
