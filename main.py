import pprint

from sqlalchemy import create_engine

from models import Base

print = pprint.pprint

engine = create_engine("sqlite:///:memory:", echo=True)

Base.metadata.create_all(engine)
