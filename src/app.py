from flask import Flask

from .config import app_config


def create_app(env_name):
    """Create app using the specified environment configurations.

    Args:
        env_name (str): the environment to run app on .eg. Development, Production
    """
    # initialise app
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])


    @app.route('/', methods=['GET'])
    def index():
        return 'Test create app function'
    
    return app