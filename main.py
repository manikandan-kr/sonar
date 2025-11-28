from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/add/{a}/{b}")
def add_numbers(a: int, b: int):
    return {"result": a + b}
