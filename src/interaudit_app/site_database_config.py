import os

from dotenv import load_dotenv

load_dotenv()


def get_database_connection():
    db = DATABASE_CONNECTION
    return db


DATABASE_CONNECTION = {

    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': os.environ.get('DB_NAME', 'interaudit'),
    'USER': os.environ.get("DB_USER", 'postgres'),
    'PASSWORD': os.environ.get("DB_PASS",'postgres'),
    'HOST': os.environ.get("DB_HOST", 'localhost'),
    'PORT': os.environ.get("DB_PORT", '5432'),

}

