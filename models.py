# -*- coding: utf-8 -*-
__author__ = 'seb'

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import createdb as cdb

engine = create_engine('sqlite:////tmp/jala.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)


# from createdb import Base


class LogEntry(Base):
    __tablename__ = 'logentry'
    id = Column(Integer, primary_key=True)
    sourceip = Column(String(500), unique=False)
    request_id = Column(String(500), unique=False)
    request_user = Column(String(500), unique=False)
    timestamp = Column(String(500), unique=False)
    request_type = Column(String(100), unique=False)
    destination = Column(String(500), unique=False)
    protocol = Column(String(100), unique=False)
    return_code = Column(String(50), unique=False)
    size = Column(String(50), unique=False)
    duration = Column(String(500), unique=False)
    referrer = Column(String(500), unique=False)
    agent = Column(String(50), unique=False)
    session = Column(String(50), unique=False)


def __init__(self, sourceip=None):
    self.sourceip = sourceip


def __repr__(self):
    return '<User %r>' % self.sourceip
