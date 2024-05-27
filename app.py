from flask import Flask
from flasgger import Swagger
from flask_restx import Api
from project.documentation import tasks_swag

import os
from dotenv import load_dotenv

from project.views import task_api
from project.database import db

load_dotenv()
URI = f'mysql://{os.getenv("USER")}:{os.getenv("PASSWORD")}@localhost/db'


def create_app(uri):
    app = Flask(__name__)

    # SQLAlchemy database config
    app.config['SQLALCHEMY_DATABASE_URI'] = uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    api_extension = Api(
        task_api,
        title='Task API',
        version='1.0',
        description='API to let you add tasks and view them',
        doc='/doc'
    )

    app.register_blueprint(task_api, url_prefix='/tasks/')
    api_extension.add_namespace(tasks_swag)

    Swagger(app)
    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app


if __name__ == '__main__':
    app = create_app(URI).run(debug=False)
