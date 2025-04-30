from flask import Flask
from biblioteca_virtual.config.settings import Config
from biblioteca_virtual.extensions import db, migrate
from dotenv import load_dotenv

from biblioteca_virtual.routes.user_routes import user_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(user_bp)
    db.init_app(app)
    migrate.init_app(app, db)

    return app