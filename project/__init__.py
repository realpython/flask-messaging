# project/__init__.py


from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from project.instance.config import app_config


# instantiate the extentions
db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name):

    # instantiate the app
    app = FlaskAPI(__name__, instance_relative_config=True)

    # set config
    app.config.from_object(app_config[config_name])

    # set up extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    from project.api.main import main_blueprint
    app.register_blueprint(main_blueprint)

    return app
