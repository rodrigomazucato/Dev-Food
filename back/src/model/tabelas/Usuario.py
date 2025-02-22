from sqlalchemy import Column, Integer, String, Boolean
from src.model.configs.base import Base

class Usuario(Base):
    __tablename__ = "Usuario"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(50))
    senha = Column(String(12))
    is_admin = Boolean