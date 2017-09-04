# project/instance/config.py


import os

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False

class DevelopmentConfig(Config):
    """Development Configurations"""
    DEBUG = True

class TestingConfig(Config):
    """Testing Configuration, with a separate test database."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_TEST_URL')
    TESTING = True

class StagingConfig(Config):
    """Staging Configuration."""
    DEBUG = True

class ProductionConfig(Config):
    """Production Configuration."""
    pass

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
