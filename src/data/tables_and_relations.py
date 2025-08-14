from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey, create_engine, Table
)
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

# Association Tables
npc_location_association = Table(
    'npc_location', Base.metadata,
    Column('npc_id', Integer, ForeignKey('npcs.id'), primary_key=True),
    Column('location_id', Integer, ForeignKey('locations.id'), primary_key=True)
)

npc_sub_location_association = Table(
    'npc_sub_location', Base.metadata,
    Column('npc_id', Integer, ForeignKey('npcs.id'), primary_key=True),
    Column('sub_location_id', Integer, ForeignKey('sub_locations.id'), primary_key=True)
)

npc_quest_association = Table(
    'npc_quest', Base.metadata,
    Column('npc_id', Integer, ForeignKey('npcs.id'), primary_key=True),
    Column('quest_id', Integer, ForeignKey('quests.id'), primary_key=True)
)

quest_location_association = Table(
    'quest_location', Base.metadata,
    Column('quest_id', Integer, ForeignKey('quests.id'), primary_key=True),
    Column('location_id', Integer, ForeignKey('locations.id'), primary_key=True)
)

quest_sub_location_association = Table(
    'quest_sub_location', Base.metadata,
    Column('quest_id', Integer, ForeignKey('quests.id'), primary_key=True),
    Column('sub_location_id', Integer, ForeignKey('sub_locations.id'), primary_key=True)
)

# Main Tables
class Plane(Base):
    __tablename__ = 'planes'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(500))
    locations = relationship("Location", back_populates="plane", cascade="all, delete-orphan")

class Location(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    plane_id = Column(Integer, ForeignKey('planes.id'), nullable=False)
    
    plane = relationship("Plane", back_populates="locations")
    sub_locations = relationship("SubLocation", back_populates="location", cascade="all, delete-orphan")
    npcs = relationship("NPC", secondary=npc_location_association, back_populates="locations")
    quests = relationship("Quest", secondary=quest_location_association, back_populates="locations")

class SubLocation(Base):
    __tablename__ = 'sub_locations'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)
    
    location = relationship("Location", back_populates="sub_locations")
    npcs = relationship("NPC", secondary=npc_sub_location_association, back_populates="sub_locations")
    quests = relationship("Quest", secondary=quest_sub_location_association, back_populates="sub_locations")

class NPC(Base):
    __tablename__ = 'npcs'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    
    locations = relationship("Location", secondary=npc_location_association, back_populates="npcs")
    sub_locations = relationship("SubLocation", secondary=npc_sub_location_association, back_populates="npcs")
    quests = relationship("Quest", secondary=npc_quest_association, back_populates="npcs")

class Quest(Base):
    __tablename__ = 'quests'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    
    locations = relationship("Location", secondary=quest_location_association, back_populates="quests")
    sub_locations = relationship("SubLocation", secondary=quest_sub_location_association, back_populates="quests")
    npcs = relationship("NPC", secondary=npc_quest_association, back_populates="quests")

# Setup DB engine and session
engine = create_engine('sqlite:///tome_of_planes.db')
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

