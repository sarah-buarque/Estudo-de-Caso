from app.extensions import db
from app.models.orders import Orders
from app.schemas.orders_schema import OrdersSchema
from app.utils.response import success_response

orders_schema = OrdersSchema()              
orders_schema = OrdersSchema(many=True)    

def criar_order(data):
    dados_validados = order_schema.load(data)

    novo_order = Orders(**dados_validados)

    db.session.add(novo_order)
    db.session.commit()

    return success_response(order_schema.dump(novo_order), 201)

def listar_orders():
    orders = Orders.query.all()
    return success_response(orders_schema.dump(orders))

def atualizar_order(id, data):
    order = Orders.query.get_or_404(id)

    dados_validados = order_schema.load(data, partial=True)

    for campo, valor in dados_validados.items():
        setattr(order, campo, valor)

    db.session.commit()

    return success_response(order_schema.dump(order))

def deletar_order(id):
    order = Orders.query.get_or_404(id)

    db.session.delete(order)
    db.session.commit()

    return "", 204