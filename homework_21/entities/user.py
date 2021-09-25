from __future__ import annotations


class User:
    def __init__(
            self,
            id,
            email,
            first_name,
            last_name,
            avatar
    ):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar

    def __eq__(self, other: User):
        return self.__dict__ == other.__dict__
