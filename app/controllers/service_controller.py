from app.extensions import db
from app.models.service import Service
from app.schemas.service_schema import ServiceSchema
from app.utils.response import success_response
from marshmallow import ValidationError

service_schema = ServiceSchema()
services_schema = ServiceSchema(many=True)


def criar_service(data):
    try:
        dados_validados = service_schema.load(data)
    except ValidationError as err:
        return {"success": False, "errors": err.messages}, 400

    novo_service = Service(**dados_validados)

    db.session.add(novo_service)
    db.session.commit()

    return success_response(service_schema.dump(novo_service), 201)


def listar_service():
    try:
        services = Service.query.all()

    
        return {
            "success": True,
            "data": [s.nome for s in services]  
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }, 500


def atualizar_service(id, data):
    service = Service.query.get_or_404(id)

    try:
        dados_validados = service_schema.load(data, partial=True)
    except ValidationError as err:
        return {"success": False, "errors": err.messages}, 400

    for campo, valor in dados_validados.items():
        setattr(service, campo, valor)

    db.session.commit()

    return success_response(service_schema.dump(service))


def deletar_service(id):
    service = Service.query.get_or_404(id)

    db.session.delete(service)
    db.session.commit()

    return {"success": True}, 204
