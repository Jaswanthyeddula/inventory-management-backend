"""Application factory and extensions setup."""
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from app.config import Config
db = SQLAlchemy()
cors = CORS()

jwt = JWTManager()
mail = Mail()
limiter = Limiter(key_func = get_remote_address)
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.json.sort_keys = False
    db.init_app(app)
    
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)
    jwt.init_app(app)
    mail.init_app(app)
    limiter.init_app(app)
    from app.models.product import Product
    from app.models.user import User
    from app.models.category import Category
    from app.models.supplier import Supplier
    # registering blueprint 
    from app.routes.dashboard import dashboard_bp
    from app.routes.auth import auth_bp
    from app.routes.category import category_bp
    from app.routes.supplier import supplier_bp
    from app.routes.product import product_bp
    from app.routes.stock import stock_bp
    app.register_blueprint(stock_bp)
    app.register_blueprint(supplier_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(product_bp)
    
    app.register_blueprint(dashboard_bp)
    
    return app