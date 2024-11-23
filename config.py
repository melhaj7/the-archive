import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'wasd'
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get('DATABASE_URL') or
        'sqlite:///' + os.path.join(basedir, 'app.db'))
    GOOGLE_API_KEY = os.getenv('API_KEY', 'MISSING_API_KEY')
    if GOOGLE_API_KEY == 'MISSING_API_KEY':
        raise ValueError('API_KEY is not set in the environment')
