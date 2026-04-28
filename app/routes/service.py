from flask import Blueprint, request, jsonify
from app.controllers.service_controller import (
    listar_service,
    criar_service,
    atualizar_service,
    deletar_service
)

service_bp = Blueprint("service", __name__)

@service_bp.route("/", methods=["GET"])
def get_service():
    response, status = listar_service()
    return jsonify(response), status

@service_bp.route("/", methods=["POST"])
def post_service():
    data = request.get_json()
    response, status = criar_service(data)
    return jsonify(response), status

@service_bp.route("/<int:id>", methods=["PATCH"])
def patch_service(id):
    data = request.get_json()
    r, s = atualizar_service(id, data)
    return jsonify(r), s

@service_bp.route("/<int:id>", methods=["DELETE"])
def delete_service(id):
    r, s = deletar_service(id)
    return jsonify(r), s


