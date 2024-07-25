from fastapi import FastAPI
from pydantic import BaseModel
from calculator import calculator

class User_Input(BaseModel):
    operation : str
    x : int
    y : int

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/calculate')
def operate(input:User_Input):
    result = calculator(input.x,input.y,input.operation)
    return result