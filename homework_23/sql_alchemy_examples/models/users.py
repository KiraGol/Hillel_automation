from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, VARCHAR, Integer

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"
    id = Column(VARCHAR(10), primary_key=True)
    name = Column(VARCHAR(50))
    email = Column(VARCHAR(50))
    age = Column(Integer)

    def __str__(self):
        return f"\n{self.id}\n{self.name}\n{self.email}\n{self.age}"