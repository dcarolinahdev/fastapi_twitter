# Twitter API in FastAPI

## Versions

```
fastapi==0.81.0
uvicorn==0.18.3

"pydantic[email]" -> email-validator==1.2.1
```
You can see complete requirements in [requirements.txt](requirements.txt)

## END-POINTS

**tweets**

| route | meaning |
| --- | --- |
| / | show all tweets |
| /post | create a tweet |
| /tweets/{tweet_id} | show a specific tweet |
| /tweets/{tweet_id}/delete | delete a specific tweet |
| /tweets/{tweet_id}/update | update a specific tweet |

**users**

| route | meaning |
| --- | --- |
| /signup | register an user |
| /login | login an user |
| /users | show all users |
| /users/{user_id} | show a specific user |
| /users/{user_id}/delete | delete a specific user |
| /users/{user_id}/update | update a specific user |

You can see complete requirements in [requirements.txt](requirements.txt)

## How to run locally this app?

```
uvicorn main:app --reload
```

## Interactive documentation

### How to show Swagger documentation?

```
http://127.0.0.1:8000/docs
```

### How to show ReDoc documentation?

```
http://127.0.0.1:8000/redoc
```
