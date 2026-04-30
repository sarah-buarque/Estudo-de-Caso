from app.extensions import db

provider_services = db.Table(
   "provider_services",
   db.Column("provider_id", db.Integer, db.ForeignKey("providers.id"), primary_key=True),
   db.Column("service_id", db.Integer, db.ForeignKey("service.id"), primary_key=True)
)
