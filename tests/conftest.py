import pytest
import os
from app import create_app, db


URI = f'mysql://{os.getenv("USER")}:{os.getenv("PASSWORD")}@localhost/fake_db'


@pytest.fixture(scope='session')
def test_app():
    app = create_app(URI)
    yield app


@pytest.fixture(scope='session')
def client(test_app):
    with test_app.app_context():
        db.drop_all()
        db.create_all()
    return test_app.test_client()
