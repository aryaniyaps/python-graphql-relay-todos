import dataclasses

from strawberry.dataloader import DataLoader

from app.notes.dataloaders import load_note_by_id
from app.notes.models import Note


@dataclasses.dataclass(slots=True, kw_only=True)
class Dataloaders:
    note_by_id: DataLoader[str, Note | None]


def create_dataloaders() -> Dataloaders:
    return Dataloaders(
        note_by_id=DataLoader(
            load_fn=load_note_by_id,
        )
    )
