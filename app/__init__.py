from flask import Flask
from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException

from .config import Config
from .extensions import db, ma, migrate


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    # 🔍 DEBUG (isolando problema do service)
    print("SERVICE IMPORT OK")

    from .routes.messages import messages_bp
    from .routes.users import users_bp
    from .routes.service import service_bp

    print("SERVICE BP LOADED")

    app.register_blueprint(messages_bp, url_prefix="/messages")
    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(service_bp, url_prefix="/services")

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
        return {"success": False, "message": "Erro interno do servidor"}, 500

    print("URL MAP:", app.url_map)

    return app