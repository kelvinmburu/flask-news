from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
    
    app = Flask(__name__)
    
    #Creating the app configurations
    app.config.from_object(config_options[config_name])


    # Initializing Flask Extensions
    bootstrap.init_app(app)
    
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    #Settings config
    from .request import configure_request
    configure_request(app)

    from app.main import error
    from app.main import views

    return app