import click
from flask import Flask, url_for, redirect

from db import Base, engine, UserRoleEnum
from db.helpers import session_scope
from db.models import User
from .api import add_resources
from .conversion import conversion_bp
from .dashboard import dashboard_bp
from .login import login_bp
from .extensions import api, flask_httpauth, swagger, flask_principal, login_manager


def register_extensions(app):
    """Register extensions on a Flask app."""

    @flask_httpauth.verify_password
    def verify_password(username, password):
        with session_scope() as session:
            user = session.query(User).filter_by(login=username).first()
            check = user and user.check_password(password)
            if check:
                session.expunge(user)
            return check and user

    @login_manager.user_loader
    def load_user(user_id):
        with session_scope() as session:
            user = session.query(User).get(user_id)
            session.expunge(user)
            return user

    @login_manager.unauthorized_handler
    def redirect_to_login():
        return redirect(url_for('login.login'))

    add_resources(api)
    api.init_app(app)
    swagger.init_app(app)
    flask_principal.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    app.register_blueprint(login_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(conversion_bp)


def register_cli(app):
    @app.cli.command(short_help='Reset database and add admin user with <login> and <password>')
    @click.argument('login')
    @click.argument('password')
    def init_db(login, password):
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        with session_scope() as session:
            user = User(login=login, role=UserRoleEnum.GLOBAL_ADMIN)
            user.hash_password(password)
            session.add(user)


def create_app(config_object='settings'):
    """Flask app factory."""

    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_cli(app)
    return app
