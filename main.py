from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Calculator(BaseModel):
    num_1: int
    num_2: int
    operation: str


@app.post("/calculator")
def calculate(numbers: Calculator):
    if numbers.operation == "+":
        return {"Result": numbers.num_1 + numbers.num_2}
    elif numbers.operation == "-":
        return {"Result": numbers.num_1 - numbers.num_2}
    elif numbers.operation == "*":
        return {"Result": numbers.num_1 * numbers.num_2}
    elif numbers.operation == "/":
        return {"Result": numbers.num_1 / numbers.num_2}
    elif numbers.operation == "**":
        return {"Result": numbers.num_1 ** numbers.num_2}

