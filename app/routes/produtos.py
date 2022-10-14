from sqlalchemy.orm import Session
from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.responses import RedirectResponse
from typing import List
# importações locais
from app.schema import schemas
from app.controller.curd import RepositorioProduto
from app.database.config import get_db

router = APIRouter()

@router.get('/', status_code = status.HTTP_200_OK)
async def root():
  response = RedirectResponse(url='/docs')
  return response

@router.get('/produto', status_code = status.HTTP_200_OK, response_model=List[schemas.Produto])
async def listar_produto(db:Session = Depends(get_db)):
  listar = RepositorioProduto(db).listar_produto()
  if not listar:
    raise HTTPException(status_code = 404, detail = 'Sem produto criado')
  return {"message": "Olá, Mundo!"}

@router.post('/produto', status_code = status.HTTP_200_OK)
async def criar_produto(produto: schemas.Produto, db: Session = Depends(get_db)):
  produto_criar = RepositorioProduto(db).criar(produto)
  return produto_criar