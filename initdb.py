from sqlalchemy import *
import datetime

engine = create_engine('sqlite:///db.sqlite')

metadata = MetaData()

user = Table('user', metadata,
    Column('id',Integer, primary_key=True),
    Column('type', String(10), nullable=False, default="patient"),
    Column('name', String(128), nullable=False),
    Column('birthdate', DateTime, default=datetime.datetime(1943,12,23)),
    Column('mobile', String(20)),
    Column('mail', String(128)),
    Column('critical', Boolean(), default=False),
    )

data = Table('data', metadata,
        Column('id', Integer, primary_key=True),
        Column('user_id', Integer, ForeignKey("user.id"), nullable=False),
        Column('origine', String(128), nullable=False),
        Column('doc_url', String(128), nullable=True),
        Column('type_data', String(128), nullable=False),
        Column('date', DateTime, default=datetime.datetime.utcnow),
        )

ldata = Table('ldata', metadata,
    Column('id', Integer, primary_key=True),
    Column('data_id', Integer, ForeignKey("data.id"), nullable=False),
    Column('unit', String(12), nullable=False),
    Column('value', String(100)),
    )

metadata.create_all(engine)
