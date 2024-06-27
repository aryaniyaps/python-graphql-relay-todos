"""
add todo completed

Revision ID: 821ce9f3d275
Revises: 1d39b1c92f55
Create Date: 2024-06-27 07:38:15.533925

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "821ce9f3d275"
down_revision: str | None = "1d39b1c92f55"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column(
        "notes",
        sa.Column("completed", sa.Boolean(), nullable=False),
    )


def downgrade() -> None:
    op.drop_column("notes", "completed")
