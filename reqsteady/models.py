from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Boolean, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.functions import now

from flask_appbuilder import Model
from flask_appbuilder.security.sqla.models import User

Base = Model


class Documents(Base):
    """
    Requirements Documents.
    """
    __tablename__ = 'Documents'
    id = Column(Integer, primary_key=True)
    handle = Column(String(256))
    #: Should usually be a reference to a document in DocuShare.
    document_type = Column(String(256))
    status = Column(String(256))
    summary = Column(Text)
    created = Column(DateTime, default=now())
    modified = Column(DateTime, default=now())
    importance = Column(String(16))
    priority = Column(String(8))

    document_owners = relationship(User, secondary="DocumentOwners", backref='Documents')
    # document_tags = relationship("DocumentTags", lazy="dynamic")
    # related_documents = relationship("RelatedDocuments", lazy="dynamic")

    def __repr__(self):
        return self.handle


document_owners = Table(
    'DocumentOwners', Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("document_id", Integer, ForeignKey("Documents.id")),
    Column("owner_id", Integer, ForeignKey(User.id))
)


class DocumentTags(Base):
    """
    Tags to facilitate the identification or grouping of requirements.
    """
    __tablename__ = 'DocumentTags'
    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, ForeignKey("Documents.id"),)
    tag = Column(String(256))

    def __repr__(self):
        return self.tag


# class RelatedDocuments(Base):
#     __tablename__ = 'RelatedDocuments'
#     id = Column(Integer, primary_key=True)
#     document_id = Column(Integer, ForeignKey("Documents.id"))
#     related_id = Column(Integer, ForeignKey("Documents.id"))


class Requirements(Base):
    """
    Requirements are the identified and named requirements
    in a Requirements Document.
    """
    __tablename__ = 'Requirements'
    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, ForeignKey("Documents.id"), nullable=False)
    document = relationship("Documents")
    req_id = Column(String(256))
    requirement_type = Column(String(256))
    status = Column(String(256))
    summary = Column(Text)
    created = Column(DateTime, default=now())
    modified = Column(DateTime, default=now())
    importance = Column(String(16))
    priority = Column(String(8))
    # specs = relationship("Specs", lazy="dynamic")
    # requirement_tags = relationship("RequirementTags", lazy="dynamic")
    # related_requirements = relationship("RelatedRequirements", lazy="dynamic")

    def __repr__(self):
        return self.req_id


class RequirementTags(Base):
    """
    Tags to facilitate the identification or grouping of requirements.
    """
    __tablename__ = 'RequirementTags'
    id = Column(Integer, primary_key=True)
    requirement_id = Column(Integer, ForeignKey("Requirements.id"))
    tag = Column(String)


# class RelatedRequirements(Base):
#     __tablename__ = 'RelatedRequirements'
#     id = Column(Integer, primary_key=True)
#     requirement_id = Column(Integer, ForeignKey("Requirements.id"))
#     related_id = Column(Integer, ForeignKey("Requirements.id"))


class Runs(Base):
    """
    A Run is effectively the execution of a document and the specs
    associated with it.
    """
    __tablename__ = 'Runs'
    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, ForeignKey("Documents.id"))
    tag = Column(String(256))
    created = Column(DateTime, default=now())
    document_owners = relationship(User, secondary="Testers", backref='Runs')


class RunConfigurations(Base):
    """
    A RunConfiguration is configuration information which is
    associated for all tests in a run. A Test's confugration
    may override this configuration.
    """
    __tablename__ = 'RunConfigurations'
    id = Column(Integer, primary_key=True)
    test_id = Column(Integer, ForeignKey("Runs.id"))
    configuration = Column(Text)
    created = Column(DateTime, default=now())
    modified = Column(DateTime, default=now())
    configuration_resources = relationship("RunConfigurationResources", lazy="dynamic")


class RunConfigurationResources(Base):
    """
    References to resources related to the RunConfiguration
    """
    __tablename__ = 'RunConfigurationResources'
    id = Column(Integer, primary_key=True)
    run_configuration_id = Column(Integer, ForeignKey("RunConfigurations.id"))
    uri = Column(String(1024))


testers = Table(
    'Testers', Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("run_id", Integer, ForeignKey("Runs.id")),
    Column("tester_id", Integer, ForeignKey(User.id))
)


class Specs(Base):
    """"
    A Test is the execution of a specification
    during a run.
    """
    __tablename__ = 'Specs'
    id = Column(Integer, primary_key=True)
    requirement_id = Column(Integer, ForeignKey("Requirements.id"))
    created = Column(DateTime, default=now())
    modified = Column(DateTime, default=now())
    inputs = Column(Text)
    criteria = Column(Text)
    outputs = Column(Text)
    qa_resources = relationship("SpecQAResources", lazy="dynamic")
    components = relationship("SpecComponents", lazy="dynamic")
    related_issues = relationship("SpecIssues", lazy="dynamic")
    # FIXME: Here we want some relationship which represents the
    # current tests for this spec, as opposed to all tests.
    # current_tests = relationship("SpecIssues", lazy="dynamic")


class SpecIssues(Base):
    """
    SpecIssues are issues, typically in Jira, related to this
    spec.
    """
    __tablename__ = 'SpecIssues'
    id = Column(Integer, primary_key=True)
    spec_id = Column(Integer, ForeignKey("Specs.id"))
    #: Jira, something else?
    issue_type = Column(String(256))
    handle = Column(String(256))


class SpecComponents(Base):
    """
    SpecComponents are the components tests by this spec.
    """
    __tablename__ = 'SpecComponents'
    id = Column(Integer, primary_key=True)
    spec_id = Column(Integer, ForeignKey("Specs.id"))
    component = Column(String(256))


class SpecQAResources(Base):
    """
    SpecQAResources are URIs that are related to a spec.
    Typically they are files, repos, commits, LSST documents,
    or some other resource.
    """
    __tablename__ = 'TestConfigurations'
    id = Column(Integer, primary_key=True)
    spec_id = Column(Integer, ForeignKey("Specs.id"))
    description = Column(Text)
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
    execution_id = Column(Integer)
    #: There may be many tests executed for a given spec and run
    is_current = Column(Boolean)
    #: Human readable summary of the execution
    summary = Column(Text)
    status = Column(String(128))
    created = Column(DateTime, default=now())
    modified = Column(DateTime, default=now())


# FIXME: Need index on (spec_id and is_current?)


class TestConfigurations(Base):
    """
    Configurations of Tests.
    """
    __tablename__ = 'TestConfigurations'
    id = Column(Integer, primary_key=True)
    test_id = Column(Integer, ForeignKey("Tests.id"))
    configuration = Column(Text)
    created = Column(DateTime, default=now())
    modified = Column(DateTime, default=now())
    configuration_resources = relationship("TestConfigurationResources", lazy="dynamic")


class TestConfigurationResources(Base):
    __tablename__ = 'TestConfigurationResources'
    id = Column(Integer, primary_key=True)
    test_configuration_id = Column(Integer, ForeignKey("TestConfigurations.id"))
    uri = Column(String(1024))
