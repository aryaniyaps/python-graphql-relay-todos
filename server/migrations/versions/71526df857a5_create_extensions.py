"""
create extensions

Revision ID: 71526df857a5
Revises:
Create Date: 2024-06-21 06:59:08.276780

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "71526df857a5"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.execute(sa.text("CREATE EXTENSION IF NOT EXISTS citext;"))


def downgrade() -> None:
    op.execute(sa.text("DROP EXTENSION IF EXISTS citext;"))
