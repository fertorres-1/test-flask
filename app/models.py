#Models.py

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date
from flask_login import UserMixin

Base = declarative_base()

class Usuario(Base, UserMixin):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

class Diario(Base):
    __tablename__ = 'diarios'
    id = Column(Integer, primary_key=True)
    fecha = Column(Date)
    actividad = Column(String)
    cantidad = Column(Float)
