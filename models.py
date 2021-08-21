import pprint
from datetime import datetime

from sqlalchemy import Column, Date, Integer, String, create_engine, ForeignKey, UniqueConstraint
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, backref

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(25), nullable=False)
    date_of_joining = Column(Date, nullable=False)
    last_login = Column(Date)

    def __repr__(self):
        return (
            f"<User{{user_id='{self.user_id}', "
            f"username='{self.username}', "
            f"date_of_joining='{self.date_of_joining}'}}>"
        )


class Artist(Base):
    __tablename__ = "artist"

    artist_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    song = relationship("Song", backref=backref("artist"))

    def __repr__(self):
        return (
            f"<Artist{{artist_id='{self.artist_id}', "
            f"name='{self.name}'}}>"
        )


class Song(Base):
    __tablename__ = "song"

    song_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    artist_id = Column(Integer, ForeignKey("artist.artist_id"))
    url = Column(String(200))

    def __repr__(self):
        return (
            f"<User{{song_id='{self.song_id}', "
            f"name='{self.name}'}}>"
        )


class SongLike(Base):
    __tablename__ = "song_like"
    __table_args__ = (UniqueConstraint(
        "song_id", "user_id", name="song_user_uniqueconstraint"),)
    song_like_id = Column(Integer, primary_key=True)
    song_id = Column(Integer, ForeignKey("song.song_id"))
    user_id = Column(Integer, ForeignKey("user.user_id"))
