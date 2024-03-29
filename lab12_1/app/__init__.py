from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import config

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
migrate = Migrate()


def create_app(config_name="default"):
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object(config.get(config_name))

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = "login"
    login_manager.login_message_category = "info"

    with app.app_context():
        from .portfolio import portfolio_blueprint
        app.register_blueprint(portfolio_blueprint)

        from .auth import auth_blueprint
        app.register_blueprint(auth_blueprint)

        from .info import info_blueprint
        app.register_blueprint(info_blueprint)

        from .todo import todo_blueprint
        app.register_blueprint(todo_blueprint)

        from .users import users_blueprint
        app.register_blueprint(users_blueprint)
        
        from .post import post_blueprint
        app.register_blueprint(post_blueprint)

    return app
