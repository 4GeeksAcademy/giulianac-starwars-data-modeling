import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table planets.
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(30))
    population = Column(Integer)
    climate = Column(String(30))
    terrain = Column(String(30))
    surface_water = Column(Integer)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table characters
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(30))
    eye_color = Column(String(30))
    skin_color = Column(String(30))
    birth_year = Column(String(30))
    gender = Column(String(30))
    homeworld = Column(String(30), ForeignKey('planets.ID'), unique=True)
    planet = relationship(Planets)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table vehicles.
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    model = Column(String(30))
    vehicle_class = Column(String(30))
    manufacturer = Column(String(30))
    cost_in_credits = Column(Integer)
    length = Column(Float)
    crew = Column(Integer)
    passengers = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(30))
    pilots = Column(String(30), ForeignKey('characters.ID'), unique=True)
    character = relationship(Characters)

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table favorites.
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.ID'), unique=True)
    character = relationship('characters')
    planet_id = Column(Integer, ForeignKey('planets.ID'), unique=True)
    planet = relationship('planets')
    vehicle_id = Column(Integer, ForeignKey('vehicles.ID'), unique=True)
    vehicle = relationship(Vehicles)

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user.
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True, nullable=False)
    password = Column(String(30), nullable=False)
    email = Column(String(30), unique=True, nullable=False)
    favorites_id = Column(Integer, ForeignKey('favorites.ID'), unique=True)
    favorite = relationship(Favorites)
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
