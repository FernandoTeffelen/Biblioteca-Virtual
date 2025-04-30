from marshmallow import Schema, fields
from marshmallow.validate import Length, OneOf

from biblioteca_virtual.models.user import Roles


class CreateUserSchema(Schema):
    username = fields.Str(required=True, validate=Length(min=1))
    password = fields.Str(required=True, validate=Length(min=6))
    role = fields.Enum(Roles, by_value=True, required=True)