from fastapi import FastAPI,Header
from pydantic import BaseModel,Field
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # اجازه درخواست از همه دامنه‌ها
    #allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],  # اجازه تمام متدهای HTTP (GET, POST, PUT, DELETE, ...)
    allow_headers=["*"],  # اجازه ارسال تمام هدرها
)

class Book(BaseModel):
    name:str=Field(min_length=1)
    author:str=Field(min_length=1)
    rating:Optional[int]=None
    category:str=Field(min_length=1)
book_var=[]
user_list=["ali","akbar","hasan"]
@app.get("/")
def readapi():
    return ("{hello}:{user}")
#header
@app.get("/items")
def read_item(accept: str = Header(None),user_agent: str = Header(None),):
    return {"accept" : accept , "user_agent" : user_agent}
#JWT authentication
@app.get("/secure-data/")
def secure_data(authorization: str = Header(None)):
    if authorization != "Bearer mysecrettoken":
        return {"error": "Unauthorized"}
    return {"message": "Access granted"}

@app.get("/headerlist/")
def headerfile(name:str=Header(None), password:str=Header(None)):
    if name in user_list and password=="123":
        return {"user": "success"}
    return {"damn":"error"}      
@app.post("/")
def postapi(book_id:int , name:Book):
    book_var.append(name)
    return(f"{book_id} is appended")

@app.get("/books")
def get_books(category: str, rating: int):
    return {"category": category, "rating": rating}


