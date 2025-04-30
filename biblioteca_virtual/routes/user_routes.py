from flask import Blueprint, request, jsonify

from biblioteca_virtual.use_cases.create_user import CreateUserUseCase

user_bp = Blueprint("user", __name__, url_prefix="/user")


@user_bp.route("/create", methods=["POST"])
def create_user():
    create_user_uc = CreateUserUseCase()
    user_id = create_user_uc.create_user(data=request.get_json())
    return jsonify({"message": "Usuário criado com sucesso.", "id": user_id}), 201
