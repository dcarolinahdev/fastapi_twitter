# Python
from uuid import UUID
from datetime import date, datetime
from typing import Optional
# Pydantic
from pydantic import BaseModel, EmailStr, Field
# FastAPI
from fastapi import FastAPI, status

app = FastAPI()

# Models
class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(
        ...
    )

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Meith"
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Spring"
    )
    birth_date: Optional[date] = Field(
        default=None
    )

class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=3,
        max_length=256
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)

# Path Operations
@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=['Index']
)
def home():
    return {"Twitter API": "Working!"}
