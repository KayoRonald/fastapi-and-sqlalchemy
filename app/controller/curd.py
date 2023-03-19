
from sqlalchemy.orm import Session
from fastapi import HTTPException

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

  def listar_id(self, produto_id: str):
    return self.db.query(models.Produtos).filter(models.Produtos.id == produto_id).first()


  def deletar(self, produto_id: str):
    item = self.db.query(models.Produtos).filter(models.Produtos.id == produto_id).first()
    print(item)
    if not item:
      raise HTTPException(
      status_code=404,
      detail=f'Nenhum produto encontrado com esse ID {produto_id}')
    self.db.delete(item)
    self.db.commit()
    # print(f'Depois da exclusão: {item}')
    return True
  
  def atualizar_produto(self, produto_id: str, produto: schemas.UpdateProduto):
    produto_bd = self.db.query(models.Produtos).filter(models.Produtos.id == produto_id)
    if not produto_bd.first():
      raise HTTPException(status_code=404, detail=f"Produto com o ID {produto_id} não encontrado")
    produto_bd.update(produto.dict(exclude_unset=True))
    self.db.commit()
    return {"message": f"Produto {produto_id} atualizado com sucesso"}