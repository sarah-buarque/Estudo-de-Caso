from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from app.controllers.auth_controller import login

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def user_login():
    data = request.get_json()

    response, status = login(data)

    return jsonify(response), status