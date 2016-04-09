import datetime
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey, Boolean

from initdb import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    type = Column(String(10), nullable=False, default="patient")
    name =  Column(String(128), nullable=False)
    birthdate =  Column(DateTime, nullable=False)
    mobile = Column(String(20))
    mail = Column(String(128))
    critical = Column(Boolean(), default=False)

class Data(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    user_id = Column('user_id', Integer, ForeignKey("user.id"), nullable=False)
    origine = Column(String(128), nullable=False)
    doc_url = Column(String(128), nullable=True)
    type_data = Column(String(128), nullable=False)
    date = Column(DateTime, default=datetime.datetime.utcnow)

class LData(Base):
    __tablename__ = 'ldata'
    id = Column(Integer, primary_key=True)
    data_id = Column('data_id', Integer, ForeignKey("data.id"), nullable=False)
    unit = Column(String(12), nullable=False)
    value = Column(String(100))
