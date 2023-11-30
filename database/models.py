from sqlalchemy import Column, Boolean, Integer, DateTime, ForeignKey, String, Float
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    nick = Column(String)
    trade_link = Column(String)
    email = Column(String, unique=True, nullable=False)
    balance = Column(Integer, default=0)
    password = Column(String)
    register_date = Column(DateTime)


class Skin(Base):
    __tablename__ = 'skins'
    skin_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    skin_name = Column(String)
    flot = Column(Float)
    # skin_photo = Column(String)
    cost_skin = Column(Integer, default=0)
    exterior = Column(String)
    user_fk = relationship(User, lazy='subquery')
    skin_date = Column(DateTime)


class SkinPhoto(Base):
    __tablename__ = 'skins_photos'
    photo_id = Column(Integer, primary_key=True, autoincrement=True)
    skin_id = Column(Integer, ForeignKey('skins.skin_id'))
    skin_fk = relationship(Skin, lazy='subquery')


class Trade(Base):
    __tablename__ = 'trades'
    trade_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    skin_id = Column(Integer, ForeignKey('skins.skin_id'))
    skin_from_id = Column(Integer, ForeignKey('skins.skin_id'))
    skin_to_id = Column(Integer, ForeignKey('skins.skin_id'))
    user_fk = relationship(User, foreign_keys=[user_id], lazy='subquery')
    skin_fk = relationship(Skin, foreign_keys=[skin_id], lazy='subquery')
    cost_skin = Column(Integer, ForeignKey('skins.cost_skin'))
    user_from = Column(Integer, ForeignKey('users.user_id'))
    user_to = Column(Integer, ForeignKey('users.user_id'))

    balance = Column(Float, ForeignKey('users.balance'))
    status = Column(Boolean, default=True)
    skin_from_fk = relationship(Skin, foreign_keys=[skin_from_id], lazy='subquery')
    skin_to_fk = relationship(Skin, foreign_keys=[skin_to_id], lazy='subquery')
    trade_date = Column(DateTime)



