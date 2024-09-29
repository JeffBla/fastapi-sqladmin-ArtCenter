from sqlalchemy import Column, Integer, String, Boolean
from database import Base, engine, Session


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    Name = Column(String(255), nullable=False)
    StudentID = Column(String(255), nullable=False, unique=True)
    Password = Column(String(255), nullable=False)
    is_admin = Column(Boolean, nullable=False)


class Activity(Base):
    __tablename__ = "activity"

    id = Column(Integer, primary_key=True)
    Name = Column(String(512), nullable=False, unique=True)
    TimeDescription = Column(String(512), nullable=False)
    Location = Column(String(512), nullable=False)
    WorkHours = Column(Integer, nullable=False)
    WorkForce = Column(Integer, nullable=False)
    WorkForceBalance = Column(Integer, nullable=False)
    Description = Column(String(1024))
    art_type_id = Column(Integer, nullable=False, foreign_key="art_type.id")


class Art_type(Base):
    __tablename__ = "art_type"

    id = Column(Integer, primary_key=True)
    Name = Column(String(512), nullable=False)


# Base.metadata.create_all(engine)
