from main import app

SECRET_KEY = 'abobado'


SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
    usuario = 'root',
    senha = '123123',
    servidor = 'localhost',
    database = 'jogoteca'
)
    
