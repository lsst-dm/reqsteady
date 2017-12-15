from marshmallow_sqlalchemy import ModelSchema
from .model import *
from flask import jsonify

class DocumentSchema(ModelSchema):
    class Meta:
        model = Document


class RequirementSchema(ModelSchema):
    class Meta:
        model = Requirement


class RunSchema(ModelSchema):
    class Meta:
        model = Run


class TestSchema(ModelSchema):
    class Meta:
        model = Test


@app.route('/api/requirements')
def hello_world():
    requirements = Requirement.query.all()
    schema = RequirementSchema(many=True)
    data = schema.dump(requirements).data
    return jsonify({"requirements": data})


@app.route('/api/requirements/{id}')
def hello_world():
    requirements = Requirement.query.all()
    schema = RequirementSchema(many=True)
    data = schema.dump(requirements).data
    return jsonify({"requirements": data})


@app.route('/api/documents')
def hello_world():
    return 'Hello World!'


@app.route('/api/reports')
def hello_world():
    return 'Hello World!'
