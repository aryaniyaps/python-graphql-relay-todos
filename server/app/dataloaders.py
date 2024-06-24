import dataclasses

from strawberry.dataloader import DataLoader

from app.todos.dataloaders import load_todo_by_id
from app.todos.models import Todo


@dataclasses.dataclass(slots=True, kw_only=True)
class Dataloaders:
    todo_by_id: DataLoader[str, Todo | None]


def create_dataloaders() -> Dataloaders:
    return Dataloaders(
        todo_by_id=DataLoader(
            load_fn=load_todo_by_id,
        )
    )
