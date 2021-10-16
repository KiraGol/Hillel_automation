from homework_23.sql_alchemy_examples.models.users import Users
from homework_23.sql_alchemy_examples.session import session


class UsersRepository:
    def __init__(self):
        self.__session = session

    def get_all(self):
        for user in self.__session.query(Users).all():
            print(user)

    def delete_by_email(self, email: str):
        self.__session.query(Users).filter_by(email=email).delete()
        self.__session.commit()

    def update_one_by_id(self, old_id: str, new_id: str):
        self.__session.query(Users).filter_by(id=old_id).update({'id': new_id})
        self.__session.commit()

    def add_one(self, user: Users):
        self.__session.add(user)
        self.__session.commit()


if __name__== '__main__':
    user_repository = UsersRepository()
    user_repository.update_one_by_id("1", "78")
    user_repository.get_all()