# project/tests/test_main.py


import json
import unittest

from project import create_app


class TestMainBlueprint(unittest.TestCase):
    """Tests for the Main Blueprint."""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client

    def test_config(self):
        """Ensure the /ping route behaves correctly."""
        self.assertTrue(self.app.config['TESTING'])
        self.assertTrue(self.app.config['DEBUG'])
        self.assertEqual(self.app.config['SECRET_KEY'], 'change_me')

    def test_main_route(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client().get('/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])


if __name__ == "__main__":
    unittest.main()
