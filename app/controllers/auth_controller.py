from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

from app.models.user import User
from app.utils.response import success_response, error_response


def login(data):
    email = data.get("email")
    senha = data.get("senha")

    if not email or not senha:
        return error_response("Email e senha são obrigatórios", 400)

    usuario = User.query.filter_by(email=email).first()

    if not usuario:
        return error_response("Email ou senha inválidos", 401)

    if not check_password_hash(usuario.senha, senha):
        return error_response("Email ou senha inválidos", 401)

    access_token = create_access_token(identity=str(usuario.id))

    return success_response({
        "access_token": access_token
    })