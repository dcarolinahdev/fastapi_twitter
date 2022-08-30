# Python
import json
from uuid import UUID
from datetime import date, datetime
from typing import Optional, List
# Pydantic
from pydantic import BaseModel, EmailStr, Field
# FastAPI
from fastapi import FastAPI, status, HTTPException
from fastapi import Body, Path

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

class UserRegister(User):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
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

## Users

### Register a user
@app.post(
    path="/signup",
    status_code=status.HTTP_201_CREATED,
    response_model=User,
    summary="Register a user",
    tags=['Users']
)
def signup(user: UserRegister = Body(...)):
    """
    **Register a user**

    This path operation register a user in the app (for now in json file).

    Parameters:
    - Request body parameter **[user : UserRegister]**:
        - A user model with: user_id, email, password, first_name, last_name and birth_date.

    Returns:
    - A **json** with the basic user information:
        - user_id (UUID), email (Emailstr), first_name (str), last_name (str) and birth_date (date).
    """
    with open("users.json", "r+", encoding="UTF-8") as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user

### Login a user
@app.post(
    path="/login",
    status_code=status.HTTP_200_OK,
    response_model=User,
    summary="Login a user",
    tags=['Users']
)
def login():
    pass

### Show all users
@app.get(
    path="/users",
    status_code=status.HTTP_200_OK,
    response_model=List[User],
    summary="Show all users",
    tags=['Users']
)
def show_all_users():
    """
    **Show all users**

    This path operation show all users in the app.

    Parameters:
    -

    Returns:
    - A **json** with all users in the app, with the following keys:
        - user_id (UUID), email (Emailstr), first_name (str), last_name (str) and birth_date (date).
    """
    with open("users.json", "r", encoding="UTF-8") as f:
        results = json.loads(f.read())
        return results

### Show a user
@app.get(
    path="/users/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=User,
    summary="Show a user",
    tags=['Users']
)
def show_a_user(
    user_id: str = Path(
        ...,
        example="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        title="User identification",
        description="This is the user_id in db"
        )
):
    """
    **Show a user if exists in the app**

    This path operation show a specific user in the app.

    Parameters:
    - **user_id: str**: User identification in database.

    Returns:
    - A python dict with identification in database as key and message as value.
    """
    with open("users.json", "r", encoding="UTF-8") as f:
        users = json.loads(f.read())
        for user in users:
            if user.get("user_id") == user_id:
                found = user
                break
        return found
    """if user_id not in users:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="This user doesn't exist!"
    )"""

### Delete a user
@app.delete(
    path="/users/{user_id}/delete",
    status_code=status.HTTP_200_OK,
    # response_model=User,
    summary="Delete a user",
    tags=['Users']
)
def delete_a_user(
    user_id: str = Path(
        ...,
        example="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        title="User identification",
        description="This is the user_id in db"
        )
):
    """
    **Delete a user**

    This path operation delete a specific user in the app.

    Parameters:
    - **user_id: str**: User identification in database.

    Returns:
    - A python dict with identification in database as key and message as value.
    """
    deleted = False
    with open("users.json", "r+", encoding="UTF-8") as f:
        users = json.loads(f.read())
        for user in users:
            if user.get("user_id") == user_id:
                users.pop(users.index(user))
                deleted = True
                break
        f.close

        with open("users.json", "w", encoding="UTF-8") as f:
            f.seek(0)
            f.write(json.dumps(users))

    return {"Deleted": str(deleted)}

### Update a user
@app.put(
    path="/users/{user_id}/update",
    status_code=status.HTTP_200_OK,
    response_model=User,
    summary="Update a user",
    tags=['Users']
)
def update_a_user(
    user_id: str = Path(
        ...,
        example="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        title="User identification",
        description="This is the user_id in db"
        ),
    user_updated: User = Body(...),
):
    """
    **Update a user**

    This path operation update a specific user in the app.

    Parameters:
    - **user_id: str**: User identification in database.

    Returns:
    - A python dict with identification in database as key and message as value.
    """
    with open("users.json", "r+", encoding="UTF-8") as f:
        users = json.loads(f.read())
        founded = None
        for user in users:
            if user.get("user_id") == user_id:
                founded = user
                break
        f.close

        user = user_updated.dict()
        user["user_id"] = str(user["user_id"])
        user["birth_date"] = str(user["birth_date"])
        users[users.index(founded)] = user

        with open("users.json", "w", encoding="UTF-8") as f:
            f.seek(0)
            f.write(json.dumps(users))

        return user
    """if user_id not in users:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="This user doesn't exist!"
    )"""

## Tweets

### Show all tweets
@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    response_model=List[Tweet],
    summary="Show all tweets",
    tags=['Tweets']
)
def home():
    """
    **Show all tweets**

    This path operation show all tweets in the app.

    Parameters:
    -

    Returns:
    - A **json** with all tweets in the app, with the following keys:
        - tweet_id (UUID), content (str), created_at (datetime), updated_at (optional - datetime) and by (User).
    """
    with open("tweets.json", "r", encoding="UTF-8") as f:
        results = json.loads(f.read())
        return results

### Post a tweet
@app.post(
    path="/post",
    status_code=status.HTTP_201_CREATED,
    response_model=Tweet,
    summary="Post a tweet",
    tags=['Tweets']
)
def post(tweet: Tweet = Body(...)):
    """
    **Post a tweet**

    This path operation post a tweet in the app (for now in json file).

    Parameters:
    - Request body parameter **[tweet : Tweet]**:
        - A tweet model with: tweet_id, content, created_at, updated_at (optional) and by.

    Returns:
    - A **json** with the basic tweet information:
        - tweet_id (UUID), content (str), created_at (datetime), updated_at (Optional datetime) and by (User).
    """
    with open("tweets.json", "r+", encoding="UTF-8") as f:
        results = json.loads(f.read())
        tweet_dict = tweet.dict()
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        tweet_dict["updated_at"] = str(tweet_dict["updated_at"])

        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"])

        results.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return tweet

### Show a tweet
@app.get(
    path="/tweets/{tweet_id}",
    status_code=status.HTTP_200_OK,
    response_model=Tweet,
    summary="Show a tweet",
    tags=['Tweets']
)
def show_a_tweet(
    tweet_id: str = Path(
        ...,
        example="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        title="Tweet identification",
        description="This is the tweet_id in db"
        )
):
    """
    **Show a tweet if exists in the app**

    This path operation show a specific tweet in the app.

    Parameters:
    - **tweet_id: str**: Tweet identification in database.

    Returns:
    - A python dict with identification in database as key and message as value.
    """
    with open("tweets.json", "r", encoding="UTF-8") as f:
        tweets = json.loads(f.read())
        for tweet in tweets:
            if tweet.get("tweet_id") == tweet_id:
                found = tweet
                break
        return found

### Delete a tweet
@app.delete(
    path="/tweets/{tweet_id}/delete",
    status_code=status.HTTP_200_OK,
    response_model=Tweet,
    summary="Delete a tweet",
    tags=['Tweets']
)
def delete_a_tweet():
    pass

### Update a tweet
@app.put(
    path="/tweets/{tweet_id}/update",
    status_code=status.HTTP_200_OK,
    response_model=Tweet,
    summary="Update a tweet",
    tags=['Tweets']
)
def update_a_tweet():
    pass
