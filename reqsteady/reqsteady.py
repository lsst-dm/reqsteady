from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_appbuilder import SQLA
from flask_appbuilder import AppBuilder
from reqsteady.api import *
from sqlalchemy.engine import Engine
from sqlalchemy import event


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

app.config.from_object('config')
db = SQLA(app, model_class=Base)
appbuilder = AppBuilder(app, db.session)
migrate = Migrate(app, db)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/requirements')
def hello_world():
    requirements = Requirement.query.all()
    return 'Hello World!'


@app.route('/documents')
def hello_world():
    return 'Hello World!'


@app.route('/reports')
def hello_world():
    return 'Hello World!'




if __name__ == '__main__':
    app.run()
