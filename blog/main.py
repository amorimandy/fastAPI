from fastapi import FastAPI
from . import schemas  # import of Base Model



app = FastAPI()


@app.post('/blog')
def create(request: schemas.Blog):
    return request
