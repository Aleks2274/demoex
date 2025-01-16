import datetime
from pydantic import BaseModel


class order(BaseModel):
    number : int
    startDate : datetime.date
    device :str
    problemType : str
    description : str
    client : str
    status : str


from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/")
def read_root():
    return "hello brat"