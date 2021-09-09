"""
First App using FastAPI w/ Python
"""

#https://fastapi.tiangolo.com/tutorial/first-steps/
from fastapi import FastAPI

#Run w/ 'uvicorn helloWorld:myFirstApp --reload'
myFirstApp = FastAPI() #Create instance of FastAPI

#Async is asynchronous: https://fastapi.tiangolo.com/async/#in-a-hurry
#Get is an HTTPS operator

@myFirstApp.get("/") #Path that the the function below us in charge of handling.
async def root():
    #This function gets called by FastAPI everytime it recievews a request to the URL "/""
    return {"message": "Hello World"}

# ~~~ Path Parameters ~~
#https://fastapi.tiangolo.com/tutorial/path-params/

#Passing variables/parameters as arguments to the function:
@myFirstApp.get("/testParameters/{parameter_id}")
async def read_item(parameter_id):
    return {"parameter_id": parameter_id}

#You pass in the argument 'parameter_id' and the function will return the same parameter back to you

#With types:

#This forces you to pass in parameter id as an integer only
@myFirstApp.get("/testParametersIntOnly/{parameter_id}")
async def read_item_int_only(parameter_id: int):
    return {"parameter_id": parameter_id}

#Passing in anything else will just throw you an error.

#Order matters:
#If you want to do something like below, you need to make sure the fixed path is declared first

@myFirstApp.get("/users/me") #The fixed path
async def read_user_me():
    return {"user_id": "the current user's id"}

@myFirstApp.get("/users/{user_id}") #The path w/ a parameter
async def read_user(user_id: str):
    return {"user_id": user_id}

#Going to localhost:8000/users/me will run the first (fixed) method
#But going to localhost:8000/users/'anything else' will run the second one

# Predefined values (enums):
from enum import Enum

#Here is a string enum:
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet  = "resnet"
    lenet   = "lenet"

#Using the enum
@myFirstApp.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Selected Alex Net"}

    if model_name == ModelName.resnet:
        return {"model_name": model_name, "message": "Selected Res Net"}

    return {"model_name": model_name, "message": "Selected Lenet"}

#Passing entire file path as an argument/parameter:
@myFirstApp.get("/files/{file_path:path}") 
async def read_files(file_path: str):
    return {"file_path": file_path}

# ~~~ Query Parameters
# fastapi.tiangolo.com/tutorial/query-params/
# Any function parameters that are not part of the path parameters are called query parameters.

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

#See that parameters are not part of path so they become query:
@myFirstApp.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    #default values of query params are set and types enforced
    return fake_items_db[skip : skip + limit]

#Query Request example:
#localhost:8000/items/?skip=0&limit=10
    
#Optional Parameters:
from typing import Optional

#Use optional library and set default to null/none:
@myFirstApp.get("/itemsOpt/{item_id}")
async def read_item_opt(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

#This works with or without the opt. query param q.
#localhost:8000/itemsOpt/hello
#localhost:8000/itemsOpt/hello/?q=thisIsOptional

#If you want to make the query parameters mandatory, then just don't give a default val
