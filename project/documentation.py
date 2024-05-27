from flask import request
from flask_restx import Namespace, Resource, fields
from datetime import datetime
from project.error_messages import VALIDATE_ERR, DELETE_MES

tasks_swag = Namespace('tasks', 'Task')

tasks_model = tasks_swag.model(
    'Task',
    {
        'id': fields.Integer(readonly=True),
        'title': fields.String(readonly=False),
        'description': fields.String(readonly=False),
        'created_at': fields.DateTime(readonly=True),
        'updated_at': fields.DateTime(readonly=True),
    },
)


test_task = [
    {
        'id': '1',
        'title': '1st Task',
        'description': 'Do smth',
        'created_at': datetime.now(),
        'updated_at':  datetime.now(),
    },
    {
        'id': '2',
        'title': '2nd Task',
        'description': 'Do smth else',
        'created_at':  datetime.now(),
        'updated_at':  datetime.now(),
    },
]


@tasks_swag.route('')
class TaskSwagClass(Resource):
    @tasks_swag.marshal_list_with(tasks_model)
    @tasks_swag.response(500, 'Internal Server Error')
    def get(self):
        return test_task, 200

    @tasks_swag.marshal_list_with(tasks_model)
    @tasks_swag.response(500, 'Internal Server Error')
    @tasks_swag.expect(tasks_model)
    def post(self):
        _ = request.get_json()
        if 'title' not in _ or 'description' not in _:
            return tasks_swag.abort(400, 'Missing data')
        if _['title'] in ['1st Task', '2nd Task']:
            return tasks_swag.abort(400, VALIDATE_ERR['err_title'])
        if len(_['title']) < 1:
            return tasks_swag.abort(400, VALIDATE_ERR['emt_title'])
        if len(_['description']) < 1:
            return tasks_swag.abort(400, VALIDATE_ERR['emt_title'])
        _['id'] = 1
        _['created_at'] = datetime.now()
        _['updated_at'] = datetime.now()
        return _, 201


@tasks_swag.route('/<int:pk>/')
class TaskSwagClassCocnrete(Resource):

    def exist_check(self, pk):
        if pk > (len(test_task) - 1):
            return tasks_swag.abort(400, 'Bad request')
        return

    @tasks_swag.marshal_list_with(tasks_model)
    @tasks_swag.response(500, 'Internal Server Error')
    def get(self, pk):
        self.exist_check(pk)
        return test_task[pk]

    @tasks_swag.marshal_list_with(tasks_model)
    @tasks_swag.expect(tasks_model)
    def put(self, pk):
        self.exist_check(pk)
        _ = request.get_json()
        if 'title' not in _ and 'description' not in _:
            return tasks_swag.abort(400, 'Missing data')
        if 'title' in _ and len(_['title']) > 0:
            test_task[pk]['title'] = _['title']
        if 'description' in _ and len(_['description']):
            test_task[pk]['description'] = _['description']
        return test_task[pk], 200

    @tasks_swag.response(500, 'Internal Server Error')
    def delete(self, pk):
        self.exist_check(pk)
        return DELETE_MES['deleted'], 204
