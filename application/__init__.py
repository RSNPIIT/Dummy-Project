from flask import Flask
from flask_login import LoginManager
from .database import db
from .models import User

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ebook.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'secret-key'
    db.init_app(app)

    # Flask-Login setup
    login_manager = LoginManager()
    login_manager.login_view = 'controllers_bp.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Import and register Blueprint
    from .controllers import controllers_bp
    app.register_blueprint(controllers_bp)

    # Create tables
    with app.app_context():
        db.create_all()

    return app
