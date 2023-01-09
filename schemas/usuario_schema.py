from typing import Optional
from typing import List

from pydantic import BaseModel, EmailStr

from schemas.artigo_schema import ArtigoSchema

class UsuarioschemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    sobrenome: str
    email: EmailStr
    eh_admin: bool = False

    class Config:
        orm_mode = True

class UsuarioSchemaCreate(UsuarioschemaBase):
    senha: str

class UsuarioSchemaArtigos(UsuarioschemaBase):
    artigos: Optional[List[ArtigoSchema]]

class UsuarioSchemaUp(UsuarioschemaBase):
    nome: Optional[str]
    sobrenome: Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]
    eh_admin: Optional[bool]






