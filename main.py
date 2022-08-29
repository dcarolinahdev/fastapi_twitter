# FastAPI
from fastapi import FastAPI, status

app = FastAPI()

@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=['Index']
)
def home():
    return {"Twitter API": "Working!"}
