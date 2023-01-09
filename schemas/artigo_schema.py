from typing import Optional

from pydantic import BaseModel, HttpUrl

class ArtigoSchema(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    url_fonte: HttpUrl

    class Config:
        orm_mode = True