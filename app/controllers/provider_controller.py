from flask import Blueprint
from app.extensions import db
from app.models.provider import Provider
from app.models.service import Service

bp = Blueprint("providers", __name__)

@bp.route("/providers/<int:id>/services/<int:service_id>", methods=["POST"])
def add_service_to_provider(id, service_id):
   provider = Provider.query.get_or_404(id)
   service = Service.query.get_or_404(service_id)

   if service not in provider.service:
       provider.service.append(service)
       db.session.commit()

   return {"message": "Serviço vinculado com sucesso"}

@bp.route("/providers/<int:id>/services", methods=["GET"])
def get_provider_services(id):
   provider = Provider.query.get_or_404(id)

   return [
       {
           "id": s.id,
           "nome": s.nome,
           "preco_base": s.preco_base
       }
       for s in provider.service
   ]

