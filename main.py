import pprint
from datetime import datetime

from sqlalchemy import Column, Date, Integer, String, create_engine
from sqlalchemy.orm import Session as SessionType
from sqlalchemy.orm import declarative_base, sessionmaker
from models import Base

print = pprint.pprint

engine = create_engine("sqlite:///:memory:", echo=True)

Base.metadata.create_all(engine)
