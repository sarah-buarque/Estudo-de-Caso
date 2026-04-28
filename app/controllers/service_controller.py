from app.extensions import db
from app.models.service import Service
from app.schemas.service_schema import ServiceSchema
from app.utils.response import success_response

service_schema = ServiceSchema()              
services_schema = ServiceSchema(many=True)    

def criar_service(data):
    dados_validados = service_schema.load(data)

    novo_service = Service(**dados_validados)

    db.session.add(novo_service)
    db.session.commit()

    return success_response(service_schema.dump(novo_service), 201)

def listar_service():
    services = Service.query.all()
    return success_response(services_schema.dump(services))

def atualizar_service(id, data):
    service = Service.query.get_or_404(id)

    dados_validados = service_schema.load(data, partial=True)

    for campo, valor in dados_validados.items():
        setattr(service, campo, valor)

    db.session.commit()

    return success_response(service_schema.dump(service))

def deletar_service(id):
    service = Service.query.get_or_404(id)

    db.session.delete(service)
    db.session.commit()

    return "", 204