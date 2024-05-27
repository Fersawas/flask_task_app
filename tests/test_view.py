from project.models import Task
import json


def test_api_post(client, test_app):
    data = {
        "title": "Test title X",
        "description": "Test description X"
    }
    test_data = json.dumps(data)
    response = client.post(
        '/tasks/',
        data=test_data,
        content_type='application/json')
    with test_app.app_context():
        assert response.status_code == 201
        assert Task.query.count() == 1
        assert Task.query.first().title == 'Test title X'


def test_api_get(client):
    response = client.get('/tasks/')
    assert response.status_code == 200
    assert len(response.get_json()) == 1


def test_json(client, test_app):
    response = client.get('/tasks/1/')
    json_response = response.get_json()
    assert 'title' in json_response
    assert 'description' in json_response
    assert 'created_at' in json_response
    assert 'updated_at' in json_response


def test_api_task_get(client):
    response = client.get('/tasks/1/')
    assert response.status_code == 200
    assert response.get_json()['title'] == "Test title X"
    assert response.get_json()['description'] == "Test description X"


def test_api_wrong_task_get(client):
    response = client.get('/tasks/12/')
    assert response.status_code == 404


def test_api_same_post(client, test_app):
    data = {
        "title": "Test title X",
        "description": "Test description X"
    }
    test_data = json.dumps(data)
    response = client.post(
        '/tasks/',
        data=test_data,
        content_type='application/json')
    with test_app.app_context():
        assert response.status_code == 400


def test_api_wrong_title_post(client, test_app):
    data = {
        "title": "",
        "description": "Test description X"
    }
    test_data = json.dumps(data)
    response = client.post(
        '/tasks/',
        data=test_data,
        content_type='application/json')
    with test_app.app_context():
        assert response.status_code == 400


def test_api_wrong_descr_post(client, test_app):
    data = {
        "title": "Another title",
        "description": ""
    }
    test_data = json.dumps(data)
    response = client.post(
        '/tasks/',
        data=test_data,
        content_type='application/json')
    with test_app.app_context():
        assert response.status_code == 400


def test_api_put(client, test_app):
    data = {
        "title": "New Title",
        "description": "New Description"
    }
    test_data = json.dumps(data)
    response = client.put(
        '/tasks/1/',
        data=test_data,
        content_type='application/json')
    with test_app.app_context():
        assert response.status_code == 200
        assert Task.query.first().title == "New Title"
        assert Task.query.first().description == "New Description"


def test_api_wrong_title_put(client, test_app):
    data = {
        "title": "",
        "description": "Description"
    }
    test_data = json.dumps(data)
    response = client.put(
        '/tasks/1/',
        data=test_data,
        content_type='application/json')
    with test_app.app_context():
        assert response.status_code == 400
        assert Task.query.first().title == "New Title"
        assert Task.query.first().description == "New Description"


def test_api_wrong_descr_put(client, test_app):
    data = {
        "title": "Title",
        "description": ""
    }
    test_data = json.dumps(data)
    response = client.put(
        '/tasks/1/',
        data=test_data,
        content_type='application/json')
    with test_app.app_context():
        assert response.status_code == 400
        assert Task.query.first().title == "New Title"
        assert Task.query.first().description == "New Description"


def test_task_delete(client, test_app):
    client.delete('/tasks/1/')
    with test_app.app_context():
        assert Task.query.count() == 0


def test_wrong_task_delete(client):
    response = client.delete('/tasks/12/')
    assert response.status_code == 404
