from marshmallow import Schema, fields, validates, ValidationError
from project.error_messages import VALIDATE_ERR
from project.models import Task
from project.database import db


class TaskSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    class Meta:
        ordered = True

    def get_item_uri(self, obj):
        return '/tasks/{obj.id}'.format(obj=obj)

    @validates('title')
    def validate_title(self, title):
        if len(title) == 0:
            raise ValidationError(
                VALIDATE_ERR['emt_title']
            )
        if Task.query.filter_by(title=title).scalar():
            raise ValidationError(
                VALIDATE_ERR['err_title']
            )

    @validates('description')
    def validate_description(self, description):
        if len(description) == 0:
            raise ValidationError(
                VALIDATE_ERR['emt_descr']
            )

    def update_task(self, task, data):
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        db.session.commit()
        return task
