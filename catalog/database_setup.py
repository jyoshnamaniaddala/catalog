import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class States(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    menu_items = relationship("MenuItem", cascade="all,delete-orphan")

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'user_id': self.user_id,
            }


class MenuItem(Base):
    __tablename__ = 'menu_item'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    ingredients = Column(String(500),nullable=False)
    image_url = Column(String(1000),nullable=False)
    description = Column(String(1000),nullable=False)
    itemtype = Column(String(100),nullable=False)
    link = Column(String(500),nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("States",
                         backref=backref("items", cascade="all,delete-orphan"))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'ingredients' : self.ingredients,
            'image_url' : self.image_url,
            'description' : self.description,
            'Type' : self.Type,
            'link' : self.link,

            }
engine = create_engine('postgresql://catalog:catalog@localhost/catalog')

Base.metadata.create_all(engine)
