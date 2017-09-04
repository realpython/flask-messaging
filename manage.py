# manage.py

import unittest
import os

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from project import db, create_app
from project.api import models


app = create_app(config_name=os.getenv('ENVIRONMENT'))
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
