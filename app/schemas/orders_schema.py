from app.extensions import ma
from app.models.orders import Orders
from marshmallow import fields

class OrdersSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Orders
        load_instance = True

    id = ma.auto_field(dump_only=True)
    descricao = ma.auto_field(required=True)
    status = ma.auto_field(required=True)
    service_id = ma.auto_field(required=True)

    service = fields.Nested(
        "ServiceSchema",
        only=("id", "nome", "descricao", "preco_base")
    )