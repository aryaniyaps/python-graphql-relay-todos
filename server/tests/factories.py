from app.todos.models import Todo
from polyfactory.factories.sqlalchemy_factory import SQLAlchemyFactory
from polyfactory.pytest_plugin import register_fixture


class BaseFactory(SQLAlchemyFactory):
    __is_base_factory__ = True


@register_fixture
class TodoFactory(BaseFactory):
    __model__ = Todo
