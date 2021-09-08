#https://fastapi.tiangolo.com/tutorial/first-steps/
from fastapi import FastAPI

#Run w/ 'uvicorn helloWorld:myFirstApp --reload'
myFirstApp = FastAPI() #Create instance of FastAPI

@myFirstApp.get("/") #Path that the the function below us in charge of handling. Get is an HTTPS operator

#Async is asynchronous: https://fastapi.tiangolo.com/async/#in-a-hurry
async def root():
    #This function gets called by FastAPI everytime it recievews a request to the URL "/" using a GET operation
    return {"message": "Hello World"}

