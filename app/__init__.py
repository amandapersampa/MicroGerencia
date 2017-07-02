# coding=utf-8
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask import render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

CORS(app)

#app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
app.run(debug=True, host='0.0.0.0')

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

from app.main.models.Produto import Produto_dao
from app.main.controllers import Produto_controller
from app.main.service import Produto_service
from app.main.controllers import Compra_controller
from app.main.controllers import Unidade_medida_controller
from app.main.service import Compra_service

@app.route("/", methods=["GET"])
def hello():
    return render_template('inicio.html')