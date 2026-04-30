from app.extensions import db

class Service(db.Model):
    __tablename__ = "service"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    preco_base = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(500), nullable=False)
    
    orders = db.relationship(
       "Orders",
       backref="service",  # corrigido
       lazy=True,
       cascade="all, delete-orphan"
   )

