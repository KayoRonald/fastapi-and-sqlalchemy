from typing import Union, Optional
from pydantic import BaseModel


class Produto(BaseModel):
  id: Optional[str] = None
  nome: str
  descricao: Union[str, None] = None
  valor: float
  class Config:
    orm_mode = True
