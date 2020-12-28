import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'resource-group-west.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'resource-group-west'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'varun'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'VaRU@95mAL'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'resoursegroupeast'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'UiVvb4Iu+6j8rJq6bB8uLi6abUP1sV4lvslaF1LGH2ZaGki/Cege8vsqV5WdVWbvX9pINuNsZO2LaWLF8FHbOw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'random-container'
