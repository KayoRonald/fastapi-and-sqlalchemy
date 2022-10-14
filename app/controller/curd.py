from sqlalchemy.orm import Session
from app.models import models
from app.schema import schemas

class RepositorioProduto():

  def __init__(self, db: Session):
    self.db = db
  
  def criar(self, produto: schemas.Produto):
    db_produto = models.Produtos(nome = produto.nome, descricao = produto.descricao, valor = produto.valor)
    self.db.add(db_produto)
    self.db.commit()
    self.db.refresh(db_produto)
    return db_produto

  def listar_produto(self):
    return self.db.query(models.Produtos).all()