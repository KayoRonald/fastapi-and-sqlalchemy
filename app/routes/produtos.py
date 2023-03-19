from sqlalchemy.orm import Session
from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.responses import RedirectResponse
from typing import List
# importações locais
from app.schema.schemas import Produto, UpdateProduto
from app.controller.curd import RepositorioProduto
from app.database.config import get_db

router = APIRouter()

@router.get('/', status_code=status.HTTP_200_OK)
async def root():
  """
  high level support for doing this and that.
  """
  response = RedirectResponse(url='/docs')
  return response

@router.get('/produto',
            status_code=status.HTTP_200_OK,
            response_model=List[Produto])
async def listar_produto(db: Session = Depends(get_db)):
  """
  high level support for doing this and that.
  """
  listar = RepositorioProduto(db).listar_produto()
  print(listar)
  if not listar:
    raise HTTPException(status_code=404, detail='Sem produto criado')
  return listar

@router.get('/produto/{user_id}',
            status_code=status.HTTP_200_OK,
            response_model=Produto)
async def listar_id(user_id: str, db: Session = Depends(get_db)):
  """
  high level support for doing this and that.
  """
  listar = RepositorioProduto(db).listar_id(user_id)
  if not listar:
    raise HTTPException(
      status_code=404,
      detail=f'Nenhum produto encontrado com esse ID {user_id}')
  return listar

@router.post('/produto', status_code=status.HTTP_200_OK)
async def criar_produto(produto: Produto, db: Session = Depends(get_db)):
  produto_criar = RepositorioProduto(db).criar(produto)
  return produto_criar

@router.put('/produto/{produto_id}', status_code=status.HTTP_200_OK)
async def atualizar(produto_id: str, produto: UpdateProduto, db: Session = Depends(get_db)):
  atualizarP = RepositorioProduto(db).atualizar_produto(produto_id, produto)
  return atualizarP

@router.delete('/produto/{produto_id}', status_code=status.HTTP_200_OK)
async def delete(produto_id: str, db: Session = Depends(get_db)):
  RepositorioProduto(db).deletar(produto_id)
  return {"message": "Produto excluído com sucesso"}