from fastapi import FastAPI
from pymongo import MongoClient
app = FastAPI()
mongo = MongoClient("mongodb://admin:password@localhost:27017/react_app")
db=mongo['react_app']
post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],

}
db
# Define a route for the root endpoint
@app.get("/api/posts")
async def read_root():
    return {"message": "Hello, World!"}
