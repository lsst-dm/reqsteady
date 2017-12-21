from marshmallow_sqlalchemy import ModelSchema
from .models import *
from flask import jsonify


class DocumentsSchema(ModelSchema):
    class Meta:
        model = Documents


class RequirementsSchema(ModelSchema):
    class Meta:
        model = Requirements


class RunsSchema(ModelSchema):
    class Meta:
        model = Runs


class TestSchema(ModelSchema):
    class Meta:
        model = Tests


