from app.extensions import db
from app.models.provider_service import provider_services

class Provider(db.Model):
   __tablename__ = "providers"

   id = db.Column(db.Integer, primary_key=True)
   nome = db.Column(db.String(255), nullable=False)

   service = db.relationship(
       "Service",
       secondary=provider_services,
       backref=db.backref("providers", lazy=True),
       lazy=True
   )
