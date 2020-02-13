from os.path import dirname, abspath, join

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

db = SQLAlchemy()


def create_app(config_class=DevConfig):
    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)
    # The following is needed if you want to map classes to an existing database
    with app.app_context():
        db.Model.metadata.reflect(db.engine)
    # If you don't have a database with records that you created in ex1 then you all need to create the database tables by uncommenting the following lines
    #from app.models import <add the names of your model classes here>
    #with app.app_context():
        #db.create_all()

    # Register Blueprints
    from app.main.routes import bp_main
    app.register_blueprint(bp_main)

    return app