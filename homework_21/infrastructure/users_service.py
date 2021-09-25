from requests import Response, get

from app import config


class UsersService:
    def __init__(self):
        self.__user_url = f"{config['host']}/users"

    def get_user(self, id: int) -> Response:
        return get(f"{self.__user_url}/{id}")
