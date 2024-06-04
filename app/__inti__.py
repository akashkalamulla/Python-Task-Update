from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, AnonymousUserMixin
from flask_bcrypt import Bcrypt
from flask_wtf import CSRFProtect

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
csrf = CSRFProtect()
migrate = Migrate()  # Add this line

class CustomAnonymousUser(AnonymousUserMixin):
    def __init__(self):
        self.username = 'Guest'

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_pyfile('../config/config.py')

    db.init_app(app)
    migrate.init_app(app, db)  # Add this line
    bcrypt.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    login_manager.anonymous_user = CustomAnonymousUser
    login_manager.login_view = 'web.login'
    login_manager.login_message_category = 'info'

    from .models.user import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .routes import web
    app.register_blueprint(web)

    from .middleware import restrict_access
    app.before_request(restrict_access)

    return app
