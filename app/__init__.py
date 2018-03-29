from flask import Flask
from app.extension import bootstrap, mail, moment, db, pagedown, migrate, login_manager
from app.controllers.main import main as main_blueprint
from app.controllers.auth import auth as auth_blueprint
from app.controllers.api_1_0 import api as api_1_0_blueprint



def create_app(config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    app.config.from_pyfile('local_config.cfg', silent=True)
    register_redis(app)
    register_extensions(app)
    register_blueprint(app)
    register_commands(app)
    return app


def register_blueprint(app):
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')


def register_redis(app):
    # redis = StrictRedis.from_url(app.config['REDIS_URL'])
    # app.redis = redis
    pass


def register_extensions(app):
    db.init_app(app)
    bootstrap.init_app(app)
    migrate.init_app(app, db)
    moment.init_app(app)
    mail.init_app(app)
    pagedown.init_app(app)
    login_manager.init_app(app)


def register_commands(app):
    # app.cli.add_command()
    pass