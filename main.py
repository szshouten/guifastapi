from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router

app = FastAPI(title='Curso API - Seguranca')
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0",port=8000,
                log_level='info', reload=True)

"""
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjczNzk5NzMzLCJpYXQiOjE2NzMxOTQ5MzMsInN1YiI6IjIifQ.hWCanrXFay5mICr66kgZP31LNFcZVUtNlzxUASLkPLc
bearer
"""