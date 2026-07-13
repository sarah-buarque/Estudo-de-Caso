from flask import Flask
from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException

from .config import Config
from .extensions import db, ma, migrate, jwt

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    jwt.init_app(app)

    print("SERVICE IMPORT OK")

    from .routes.messages import messages_bp
    from .routes.users import users_bp
    from .routes.service import service_bp
    from .routes.orders import orders_bp 
    from .routes.auth import auth_bp

    print("SERVICE BP LOADED")

    app.register_blueprint(messages_bp, url_prefix="/messages")
    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(service_bp, url_prefix="/services")
    app.register_blueprint(orders_bp, url_prefix="/orders")
    app.register_blueprint(auth_bp) 

    @app.errorhandler(ValidationError)
    def handle_validation_error(err):
        return {"success": False, "errors": err.messages}, 400

    @app.errorhandler(404)
    def handle_404(err):
        return {"success": False, "message": "Recurso nao encontrado"}, 404

    @app.errorhandler(Exception)        
    def handle_generic_exception(e):
        if isinstance(e, HTTPException):
            return e

        import traceback
        traceback.print_exc()

        return {
            "success": False,
            "message": str(e)
        }, 500


    print("URL MAP:", app.url_map)

    return app