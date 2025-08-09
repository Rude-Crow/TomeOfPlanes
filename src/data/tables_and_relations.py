from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey, create_engine
)
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class Plane(Base):
    __tablename__ = 'planes'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text)

    locations = relationship("Location", back_populates="plane", cascade="all, delete-orphan")

class Location(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    plane_id = Column(Integer, ForeignKey('planes.id'))

    plane = relationship("Plane", back_populates="locations")
    npcs = relationship("NPC", back_populates="location", cascade="all, delete-orphan")

class NPC(Base):
    __tablename__ = 'npcs'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(String)
    location_id = Column(Integer, ForeignKey('locations.id'))

    location = relationship("Location", back_populates="npcs")
    quests = relationship("Quest", back_populates="npc", cascade="all, delete-orphan")

class Quest(Base):
    __tablename__ = 'quests'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    npc_id = Column(Integer, ForeignKey('npcs.id'))

    npc = relationship("NPC", back_populates="quests")

# Setup DB engine and session
engine = create_engine('sqlite:///tome_of_planes.db')
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

