from flask import Flask
from config import Config


# db = SQLAlchemy()
# migrate = Migrate()
# login = LoginManager()
# login.login_view = 'auth.login'
# login.login_message = _l('Please log in to access this page.')
# mail = Mail()
# bootstrap = Bootstrap()
# moment = Moment()
# babel = Babel()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # db.init_app(app)
    # migrate.init_app(app, db)
    # login.init_app(app)
    # mail.init_app(app)
    # bootstrap.init_app(app)
    # moment.init_app(app)
    # babel.init_app(app)

    # Blueprints
    # from app.admin import bp as admin_bp
    # app.register_blueprint(admin_bp, url_prefix='/admin')
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)    
    

    if not app.debug and not app.testing:
        # ... no changes to logging setup
        pass

    return app

# from app.main import routes