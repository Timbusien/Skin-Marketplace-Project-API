from sqlalchemy import Column, Integer, DateTime, ForeignKey, String, Float
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    nick = Column(String)
    trade_link = Column(String)
    email = Column(String)
    password = Column(String)
    profile_photo = Column(String)
    register_date = Column(DateTime)


class Skin(Base):
    __tablename__ = 'skins'
    skin_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    skin_name = Column(String)
    skin_date = Column(DateTime)
    flot = Column(Float)
    exterior = Column(String)
    user_fk = relationship(User, lazy='subquery')


class SkinPhoto(Base):
    __tablename__ = 'skins_photos'
    photo_id = Column(Integer, primary_key=True, autoincrement=True)
    skin_id = Column(Integer, ForeignKey('skins.skin_id'))
    skin_photo_fk = relationship(Skin, lazy='subquery')
    skin_fk = relationship(Skin, lazy='subquery')


class Trade(Base):
    __tablename__ = 'trades'
    trade_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    skin_id = Column(Integer, ForeignKey('skins.skin_id'))
    user_fk = relationship(User, lazy='subquery')
    skin_fk = relationship(Skin, lazy='subquery')


