# Python
from uuid import UUID
from datetime import date, datetime
from typing import Optional, List
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

## Users

@app.post(
    path="/signup",
    status_code=status.HTTP_201_CREATED,
    response_model=User,
    summary="Register a user",
    tags=['Users']
)
def signup():
    pass

@app.post(
    path="/login",
    status_code=status.HTTP_200_OK,
    response_model=User,
    summary="Login a user",
    tags=['Users']
)
def login():
    pass

@app.get(
    path="/users",
    status_code=status.HTTP_200_OK,
    response_model=List[User],
    summary="Show all users",
    tags=['Users']
)
def show_all_users():
    pass

@app.get(
    path="/users/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=User,
    summary="Show a user",
    tags=['Users']
)
def show_a_user():
    pass

@app.delete(
    path="/users/{user_id}/delete",
    status_code=status.HTTP_200_OK,
    response_model=User,
    summary="Delete a user",
    tags=['Users']
)
def delete_a_user():
    pass

@app.put(
    path="/users/{user_id}/update",
    status_code=status.HTTP_200_OK,
    response_model=User,
    summary="Update a user",
    tags=['Users']
)
def update_a_user():
    pass

## Tweets
