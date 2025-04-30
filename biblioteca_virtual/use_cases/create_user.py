from marshmallow import ValidationError

from biblioteca_virtual.dao.user_dao import UserDao
from biblioteca_virtual.models.user import User
from biblioteca_virtual.schemas.user_schemas import CreateUserSchema


class CreateUserUseCase:
    def create_user(self,data):
        schema = CreateUserSchema()
        data = schema.load(data)

        user = User(**data)

        user_dao = UserDao()

        return user_dao.create(user)


