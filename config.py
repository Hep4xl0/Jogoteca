from main import app
import os
SECRET_KEY = 'abobado'


SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
    usuario = 'root',
    senha = '123123',
    servidor = 'localhost',
    database = 'jogoteca'
)

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
