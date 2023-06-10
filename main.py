from fastapi import FastAPI

from app import api
from app.env import env

prefix = "/api"

if env.bool('PROD'):
    app = FastAPI(docs_url=None, redoc_url=None)
else:
    app = FastAPI(
        version='1.2.0',
        openapi_url=f'{prefix}/openapi.json',
        docs_url=f'{prefix}/docs'
    )

app.include_router(api.app, prefix=prefix)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=9000, reload=True)
