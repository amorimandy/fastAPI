from fastapi import FastAPI  # importing fastAPI
from typing import Optional

app = FastAPI()  # creating a instance of the app


# @app.get('/blog')
# # decorating (@app) a definition to be a web path ('/'); get operation - referring a method
# def index():  # definition/function / this function is called path operation function
#     # path returning all publications
#     return {'data': 'blog list'}


# get method using query params
@app.get('/blog')  # /blog?limit=32&published=false  -> example to be used as path on browser
def index(limit=20, published: bool = True, sort: Optional[str] = None):
    # those 2 first params are required and have a default value
    if published:
        return {'data': f'{limit} published blogs from db'}
    else:
        return {'data': 'blog list'}


@app.get('/blog/unpublished')
# this one can only appear before the dynamic route (when they have the same type), because when it's called, it'll verify if the statement is true, if not it'll try the next one
def unpublished_blogs():
    # path returning only unpublished blogs
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
# dynamic route
def get_blog_by_id(id: int):  # defining that id can only be numbers, wont accept other types of variables
    # fetch blog with id == id
    return {'data': f'number {id} publication'}


@app.get('/blog/{id}/comments')
def get_comments_by_blog_id(id, limit=10):
    # fetch comments of publications with id == id
    return {'data': {'1', '2'}}

# pydantic performs all the data validation
