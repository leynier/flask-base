from flask import current_app
from app import create_app


class TestCaseBasics:

    def test_app_exists(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        assert not current_app is None
        self.app_context.pop()

    def test_app_is_testing(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        assert current_app.config['TESTING']
        self.app_context.pop()
