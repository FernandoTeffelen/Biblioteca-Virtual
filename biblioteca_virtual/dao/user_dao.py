from sqlalchemy import Integer
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from biblioteca_virtual.exceptions.generic_exceptions import UnexpectedError
from biblioteca_virtual.exceptions.user_exceptions import UserAlreadyExists, UserNotFound, WrongPassword
from biblioteca_virtual.extensions import db
from biblioteca_virtual.models.user import User


class UserDao:
    def get_by_id(self, user_id: Integer):
        user = User.query.get(user_id)
        if user is None:
            raise UserNotFound()
        return user

    def get_by_username(self, username: str):
        user = User.query.get(username)
        if user is None:
            raise UserNotFound()
        return user

    def create(self, new_user: User):
        try:
            db.session.add(new_user)
            db.session.commit()
            return new_user.id
        except IntegrityError:
            db.session.rollback()
            raise UserAlreadyExists(f"O usuário {new_user.username} já está cadastrado.")
        except SQLAlchemyError as e:
            db.session.rollback()
            raise UnexpectedError(f"Erro inesperado: {e}")

    def update(self, user_id: Integer, new_username: str, new_password: str):
        user = self.get_by_id(user_id)
        if new_username:
            user.username = new_username

        if new_password:
            user.password = new_password

        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise UserAlreadyExists(f"O usuário {new_username} já está cadastrado.")
        except SQLAlchemyError as e:
            db.session.rollback()
            raise UnexpectedError(f"Erro inesperado: {e}")

    def authenticate(self, username: str, password: str):
        user: User = self.get_by_username(username)
        if user:
            if user.password == password:
                return user.id
            else:
                raise WrongPassword()
        else:
            raise UserNotFound()

    def delete(self, user_id: Integer):
        try:
            db.session.delete(User.query.get(user_id))
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise UserNotFound()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise UnexpectedError(f"Erro inesperado: {e}")
