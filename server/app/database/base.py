from datetime import datetime

from sqlalchemy import DateTime, MetaData
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, registry

database_metadata = MetaData(
    naming_convention={
        "ix": "%(column_0_label)s_idx",
        "uq": "%(table_name)s_%(column_0_name)s_key",
        "ck": "%(table_name)s_%(constraint_name)s_check",
        "fk": "%(table_name)s_%(column_0_name)s_fkey",
        "pk": "%(table_name)s_pkey",
    },
)


class Base(AsyncAttrs, DeclarativeBase):
    metadata = database_metadata

    registry = registry(
        type_annotation_map={
            datetime: DateTime(
                timezone=True,
            ),
        },
    )

    __mapper_args__ = {"eager_defaults": True}  # noqa: RUF012
