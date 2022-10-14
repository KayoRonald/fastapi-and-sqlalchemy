from sqlalchemy import Column, Integer, String, Float
from app.database.config import Base

class Produtos(Base):
  __tablename__ = "produtos"
  
  id = Column(Integer, primary_key=True, index=True)
  nome = Column(String(255))
  descricao = Column(String(255))
  valor = Column(Float)