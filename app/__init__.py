# coding=utf-8
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from os import environ
import os
from flask import render_template

app = Flask(__name__)

CORS(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
errors = {
    'sqlalchemy.exc.IntegrityError': {
        'message': "A user with that username already exists.",
        'status': 409,
    },
    'ResourceDoesNotExist': {
        'message': "A resource with that ID no longer exists.",
        'status': 410,
        'extra': "Any extra information you want.",
    },
}

if environ.get('HEROKU') is None:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/microblog.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('microblog startup')

if os.environ.get('HEROKU') is not None:
    import logging
    app.config['SQLALCHEMY_DATABASE_URI'] = environ['DATABASE_URL']
    stream_handler = logging.StreamHandler()
    app.logger.addHandler(stream_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('microgerencia startup')
    db.create_all()

from app.main.models.Produto import Produto_dao
from app.main.models.Item_cardapio import Item_cardapio_dao
from app.main.controllers import Produto_controller
from app.main.service import Produto_service
from app.main.controllers import Compra_controller
from app.main.controllers import Unidade_medida_controller
from app.main.controllers import Item_cardapio_controller
from app.main.controllers import  Pedido_controller
from app.main.controllers import Despesa_controller
from app.main.controllers import home_controller
from app.main.controllers import estoque_controller
from app.main.service import Compra_service