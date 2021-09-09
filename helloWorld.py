#https://fastapi.tiangolo.com/tutorial/first-steps/
from fastapi import FastAPI

#Run w/ 'uvicorn helloWorld:myFirstApp --reload'
myFirstApp = FastAPI() #Create instance of FastAPI

#Async is asynchronous: https://fastapi.tiangolo.com/async/#in-a-hurry
@myFirstApp.get("/") #Path that the the function below us in charge of handling. Get is an HTTPS operator
async def root():
    #This function gets called by FastAPI everytime it recievews a request to the URL "/" using a GET operation
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
async def read_item_intOnly(parameter_id: int):
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
@myFirstApp.get("/files/{file_path:path}") #It is conventionish to put a double slash before the file path to make it easier to read, but not needed
async def read_files(file_path: str):
    return {"file_path": file_path}

    