from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql.functions import now

from flask_appbuilder import Model

Base = Model


class Document(Base):
    __tablename__ = 'Document'
    id = Column(Integer, primary_key=True)


class Requirement(Base):
    __tablename__ = 'Requirement'
    id = Column(Integer, primary_key=True)
    document_id = Column(Integer)
    tag = Column(String(256))
    type = Column(String(256))
    status = Column(String(256))
    summary = Column(Text())
    created = Column(DateTime, default=now())
    modified = Column(DateTime, default=now())
    importance = Column(String(16))
    priority = Column(String(8))


class Run(Base):
    __tablename__ = 'Run'
    id = Column(Integer, primary_key=True)
    tag = Column(String(256))
    created = Column(DateTime, default=now())


class Test(Base):
    """"
    A Test is the execution of a requirement
    during a run.
    """
    __tablename__ = 'Test'
    id = Column(Integer, primary_key=True)
    run_id = Column(Integer)
    requirement_id = Column(Integer)
    created = Column(DateTime, default=now())
    modified = Column(DateTime, default=now())

