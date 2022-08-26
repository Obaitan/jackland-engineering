from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'admin.login'
login.login_message = 'Please log in to access this page.'
mail = Mail()
# moment = Moment()
# babel = Babel()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # db.init_app(app)
    # migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)
    # moment.init_app(app)
    # babel.init_app(app)

    # Blueprints
    from app.admin import bp as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
        

    if not app.debug and not app.testing:
        # ... no changes to logging setup
        pass

    return app

# from app.main import routes