from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import now

from flask_appbuilder import Model

Base = Model


class Users(Base):
    id = Column(Integer, primary_key=True)


class Documents(Base):
    __tablename__ = 'Documents'
    id = Column(Integer, primary_key=True)
    handle = Column(String(256))
    type = Column(String(256))
    status = Column(String(256))
    summary = Column(Text())
    created = Column(DateTime, default=now())
    modified = Column(DateTime, default=now())
    importance = Column(String(16))
    priority = Column(String(8))

    document_owners = relationship("DocumentOwners", lazy="dynamic")
    document_tags = relationship("DocumentTags", lazy="dynamic")
    # related_documents = relationship("RelatedDocuments", lazy="dynamic")


class DocumentOwners(Base):
    __tablename__ = 'DocumentOwners'
    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, ForeignKey("Documents.id"))
    owner_id = Column(Integer, ForeignKey("Users.id"))


class DocumentTags(Base):
    __tablename__ = 'DocumentOwners'
    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, ForeignKey("Documents.id"))
    owner_id = Column(Integer, ForeignKey("Users.id"))


# class RelatedDocuments(Base):
#     __tablename__ = 'RelatedDocuments'
#     id = Column(Integer, primary_key=True)
#     document_id = Column(Integer, ForeignKey("Documents.id"))
#     related_id = Column(Integer, ForeignKey("Documents.id"))


class Requirements(Base):
    __tablename__ = 'Requirements'
    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, ForeignKey("Documents.id"))
    handle = Column(String(256))
    type = Column(String(256))
    status = Column(String(256))
    summary = Column(Text())
    created = Column(DateTime, default=now())
    modified = Column(DateTime, default=now())
    importance = Column(String(16))
    priority = Column(String(8))
    testspecs = relationship("TestSpecs", lazy="dynamic")
    requirement_tags = relationship("RequirementTags", lazy="dynamic")
    # related_requirements = relationship("RelatedRequirements", lazy="dynamic")


class RequirementTags(Base):
    __tablename__ = 'RequirementTags'
    id = Column(Integer, primary_key=True)
    requirement_id = Column(Integer, ForeignKey("Requirements.id"))
    tag = Column(String)


# class RelatedRequirements(Base):
#     __tablename__ = 'RelatedRequirements'
#     id = Column(Integer, primary_key=True)
#     requirement_id = Column(Integer, ForeignKey("Requirements.id"))
#     related_id = Column(Integer, ForeignKey("Requirements.id"))


class Run(Base):
    __tablename__ = 'Run'
    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, ForeignKey("Documents.id"))
    id = Column(Integer, primary_key=True)
    tag = Column(String(256))
    created = Column(DateTime, default=now())


class RunConfigurations(Base):
    __tablename__ = 'RunConfigurations'
    id = Column(Integer, primary_key=True)
    test_id = Column(Integer, ForeignKey("Runs.id"))
    configuration_text = Column(Text())
    created = Column(DateTime, default=now())
    modified = Column(DateTime, default=now())
    configuration_resources = relationship("RunConfigurationResources", lazy="dynamic")


class RunConfigurationResources(Base):
    __tablename__ = 'RunConfigurationResources'
    id = Column(Integer, primary_key=True)
    run_configuration_id = Column(Integer, ForeignKey("RunConfugirations.id"))
    uri = Column(String(1024))


class Testers(Base):
    __tablename__ = 'Testers'
    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, ForeignKey("Documents.id"))
    tester_id = Column(Integer, ForeignKey("Users.id"))


class Specs(Base):
    """"
    A Test is the execution of a specification
    during a run.
    """
    __tablename__ = 'Specs'
    id = Column(Integer, primary_key=True)
    requirement_id = Column(Integer)
    created = Column(DateTime, default=now())
    modified = Column(DateTime, default=now())
    inputs = Column(Text())
    criteria = Column(Text())
    outputs = Column(Text())
    qa_resources = relationship("SpecQAResources", lazy="dynamic")
    components = relationship("SpecComponents", lazy="dynamic")
    related_issues = relationship("SpecIssues", lazy="dynamic")


class SpecIssues(Base):
    __tablename__ = 'SpecIssues'
    id = Column(Integer, primary_key=True)
    spec_id = Column(Integer, ForeignKey("Specs.id"))
    #: Jira, something else?
    issue_type = Column(String(256))
    handle = Column(String(256))


class SpecQAResources(Base):
    __tablename__ = 'TestConfigurations'
    id = Column(Integer, primary_key=True)
    spec_id = Column(Integer, ForeignKey("Specs.id"))
    description = Column(Text())
    uri = Column(String(1024))


class Tests(Base):
    """"
    A Test is the execution of a specification
    during a run.
    """
    __tablename__ = 'Tests'
    id = Column(Integer, primary_key=True)
    run_id = Column(Integer)
    spec_id = Column(Integer, ForeignKey("Specs.id"))
    created = Column(DateTime, default=now())
    modified = Column(DateTime, default=now())


class TestConfigurations(Base):
    __tablename__ = 'TestConfigurations'
    id = Column(Integer, primary_key=True)
    test_id = Column(Integer, ForeignKey("Tests.id"))
    configuration_text = Column(Text())
    created = Column(DateTime, default=now())
    modified = Column(DateTime, default=now())
    configuration_resources = relationship("TestConfigurationResources", lazy="dynamic")


class TestConfigurationResources(Base):
    __tablename__ = 'TestConfigurationResources'
    id = Column(Integer, primary_key=True)
    test_configuration_id = Column(Integer, ForeignKey("TestConfugirations.id"))
    uri = Column(String(1024))
