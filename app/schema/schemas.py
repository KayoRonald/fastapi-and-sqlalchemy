from typing import Union, Optional
from pydantic import BaseModel

class Produto(BaseModel):
  """Return the pathname of the KOS root directory."""
  id: Optional[str] = None
  nome: str
  descricao: Union[str, None] = None
  valor: float
  class Config: # [missing-class-docstring]
    orm_mode = True
  
class UpdateProduto(BaseModel):
  """Return the pathname of the KOS root directory."""
  nome: Optional[str]
  descricao: Optional[str]
  valor: Optional[float]
  class Config: # [missing-class-docstring]
    orm_mode = True
