from fastapi import FastAPI #importing fastAPI

app = FastAPI() #creating a app to instance fastAPI


@app.get('/') #decorating a definition to be a web path, the main one "/"; get operational
def index(): #definition/function
    return {'data': {'name': 'Andressa'}}


@app.get('/about')
def about():
    return {'data': 'about page'}
