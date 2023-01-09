from typing import List

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://geek:university@localhost:5432/faculdade'
    DBBaseModel = declarative_base()

    JWT_SECRET: str = 'tD--a3dzedf0NQPcamHUF-5r2pVlriiC5Ksme36ieG8'
    ALGORITHM: str = 'HS256'

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True

settings: Settings = Settings()
