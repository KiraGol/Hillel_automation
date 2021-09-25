import pytest

from entities.user import User
from infrastructure.users_service import UsersService


@pytest.fixture(scope="session")
def user_service():
    yield UsersService()


@pytest.fixture
def first_user():
    yield User(
        id=1,
        email="george.bluth@reqres.in",
        first_name="George",
        last_name="Bluth",
        avatar="https://reqres.in/img/faces/1-image.jpg",
    )
