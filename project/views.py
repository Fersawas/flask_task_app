from flask import request, jsonify, Blueprint
from marshmallow import ValidationError
from http import HTTPStatus

from project.schemas import TaskSchema
from project.models import Task
from project.database import db
from project.error_messages import DELETE_MES

task_api = Blueprint('task_api', __name__)


@task_api.route('/', methods=['GET'])
@task_api.route('/<int:pk>/', methods=['GET', 'DELETE', 'PUT'])
def retrieve_tasks(pk=None):
    if pk:
        task = Task.query.get_or_404(pk)

        if request.method == 'DELETE':
            db.session.delete(task)
            db.session.commit()
            return DELETE_MES['deleted'], HTTPStatus.NO_CONTENT.phrase

        if request.method == 'PUT':
            data = request.get_json()
            schema = TaskSchema()
            try:
                validated_data = schema.load(data, partial=True)
            except ValidationError as error:
                return error.messages, HTTPStatus.BAD_REQUEST
            task_upd = schema.update_task(task, validated_data)
            return jsonify(schema.dump(task_upd)), HTTPStatus.OK

        schema = TaskSchema().dump(task)
        return jsonify(schema)
    tasks = Task.query.all()
    schema = TaskSchema(many=True).dump(tasks)
    return jsonify(schema), HTTPStatus.OK


@task_api.route('/', methods=['POST'])
def create_task():
    data = request.get_json()
    schema = TaskSchema()
    try:
        validated_data = schema.load(data)
    except ValidationError as error:
        return error.messages, HTTPStatus.BAD_REQUEST
    task = Task(**validated_data)
    db.session.add(task)
    db.session.commit()
    return jsonify(schema.dump(task)), HTTPStatus.CREATED
