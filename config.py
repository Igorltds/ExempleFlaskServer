import os

class Config():
    CSRF_ENABLE = True
    SECRET = '314159265'
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    TEMPLETE_FOLDER = os.path.join(ROOT_DIR, 'templates')
    APP = None 
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconncector://tiago.silva2:de_m7jBG^WZ=0localhost:3306\dashboard_flask'

class DevelopmentConfig(Config):
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}'


class TestingConfig(Config):
    pass


app_config = {
    'development' : DevelopmentConfig(), 
    'testing' : TestingConfig()
}

app_active = os.getenv('FLASK_ENV') # Isso à baixo é ignorado, não funciona. para setar modo development só antes da execução

''' 
if app_active is None: 
    app_active = 'development' 
'''
    # O certo é dizer qual tipo de env vc quer usar logo anstes de iniciar o código:
    # export FLASK_ENV=development
