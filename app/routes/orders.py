from flask import Blueprint, request, jsonify
from app.controllers.orders_controller import (
    listar_orders,
    criar_order,
    atualizar_order,
    deletar_order
)

orders_bp = Blueprint("orders", __name__)

@orders_bp.route("/", methods=["GET"])
def get_orders():
    response, status = listar_orders()
    return jsonify(response), status

@orders_bp.route("/", methods=["POST"])
def post_order():
    data = request.get_json()
    response, status = criar_order(data)
    return jsonify(response), status

@orders_bp.route("/<int:id>", methods=["PATCH"])
def patch_order(id):
    data = request.get_json()
    response, status = atualizar_order(id, data)
    return jsonify(response), status

@orders_bp.route("/<int:id>", methods=["DELETE"])
def delete_order(id):
    _, status = deletar_order(id)
    return "", status