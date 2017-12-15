from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from reqsteady.model import *
from reqsteady.api import *


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app, model_class=Base)
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
