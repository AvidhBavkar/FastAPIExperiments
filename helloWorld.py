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

#Change for git stuff