import os

class Config:
    SECRET_KEY = 'acd6b60c667a94557bce0aec3c409354'
    SQLALCHEMY_DATABASE_URI = ''
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TSL = True
    MAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
    
    
class ProdConfig(Config):
#    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("://", "ql://", 1)
    
    
    
    
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''


config_options = {
'development':DevConfig,
'production':ProdConfig
}