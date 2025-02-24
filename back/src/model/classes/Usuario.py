from sqlalchemy import Column, Integer, String, Boolean
from back.src.model.settings.base import Base

class Usuario(Base):
    __tablename__ = "Usuario"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50))
    email = Column(String(50), unique=True)
    senha = Column(String(12))
    is_admin = Boolean