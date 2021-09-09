"""
Second Project for learning FastAPI, this one will contain further concepts like request bodies
"""

from typing import Optional #For making parameters optional

from fastapi import FastAPI
from pydantic import BaseModel #This is new for making request bodies

#Create a data model that inherits from BaseModel:
class Item(BaseModel):
    #Some attributes about the item:
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    
app = FastAPI() #Create instance of FastAPI

"""
Creates an item
"""
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        #You can access attributes of the Item like this:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

"""
Creates an item with an item id and query parameters
"""
@app.put("/items/{item_id}") #Item ID is a path param
async def create_item_params(item_id: int, item: Item, q: Optional[str] = None):
    #item is request body since it is pydantic model
    #q is a query param since not in path and primitive
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

#FastAPI can do all of those parameters above:
# If parameter is also declared in path -> Path parameter
# If parameter is singular/primitive -> Query parameter
# If parameter is type of Pydantic model -> Request Body

## Using Query:
from fastapi import Query

app.get("/getItems/")
async def read_items(q: Optional[str] = Query(None, max_length=50)):
    #This will say that q will still be optional, but if it is set,
    #the max length will be 50 characters

    #You could also have a min_length argument above 
    #The first "None" can be replaced w/ a string like "default" to set default

    #If you need to use Query but also not declare a default value for q, like
    #if you need q to be mandatory, you can replace 'None' with '...'
    #That will let FastAPI know that the parameter is required

    #You could also add regex to the end of the Query, but idk much about that
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})

# Query List/Multiple Values
from typing import List

app.get("/getItemsList/")
async def read_items_list(q: Optional[List[str]] = Query(None)):
    query_items = {"q": q}
    return query_items

#This method can accept a list of strings that will all be stored in 'q'
#Example url: localhost:8000/items/?q=foo&q=bar
#Example response: {"q": [ "foo", bar]}

# ~~~ Using Path ~~~
#Just like how you can validate stuff for query, you can also do this for Path
from fastapi import Path

@app.get("pathItems/{item_id}")
async def read_items_path(
    #Enforces that item_id is greater than or equal to 1
    #Also can do gt (greater than), lt (less than), le (less or equal)
    item_id: int = Path(..., title = "The ID of the item to get", ge=1),
    q: Optional[str] = Query(None, alias = "item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results 

