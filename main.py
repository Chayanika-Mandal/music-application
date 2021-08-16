from datetime import datetime

from sqlalchemy import Column, Date, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///:memory:", echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = "users"

    pk = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(25), nullable=False)
    date_of_joining = Column(Date, nullable=False)
    last_login = Column(Date)

    def __repr__(self):
        return f"<User(pk='{self.pk}', username='{self.username}')>"


Base.metadata.create_all(engine)
now = datetime.now()

session = Session()
john = User(username="john", password="password1234", date_of_joining=now)
session.add(john)
session.commit()
print(session.query(User).all())

session = Session()
mary = User(
    username="mary", password="password1234", date_of_joining=now, last_login=now
)
bart = User(username="bart", password="password1234", date_of_joining=now)
bob = User(username="bob", password="password1234", date_of_joining=now)
session.add_all([mary, bart, bob])
session.commit()

print(session.query(User).all())
