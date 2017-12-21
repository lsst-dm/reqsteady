from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from .models import User, Requirements, Documents
from reqsteady import appbuilder, db
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class DocumentsView(ModelView):
    datamodel = SQLAInterface(Documents)
    list_columns = ['handle', 'document_type']


class RequirementsView(ModelView):
    datamodel = SQLAInterface(Requirements)
    list_columns = ['document.handle', 'req_id', 'type', 'status', 'summary',
                    'created', 'importance', 'priority'
                    ]

    edit_form_extra_fields = {'document':  QuerySelectField('Documents',
                                query_factory=db.session.query(Documents),
                                widget=Select2Widget(extra_classes="readonly"))}
    show_template = 'appbuilder/general/model/show_cascade.html'



appbuilder.add_view(DocumentsView,
                    "List Documents",
                    icon="fa-folder-open-o",
                    category="Documents",
                    category_icon="fa-envelope")

appbuilder.add_view(RequirementsView,
                    "Requirements",
                    icon="fa-folder-open-o",
                    category="Documents",
                    category_icon="fa-envelope")