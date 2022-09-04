# Twitter API in FastAPI

---

> ***v1.2*** - This is an initial project in a learning path, it isn't finished yet and it currently includes topics such as:

*Some features*

- The models, views and forms of this project are in the same file.

- The project don't use a user interface other than documentation views, such as swagger or redoc.

- It uses base authentication.

- The project does not use any database.

- Validations: Query and Path Parameters.

- Preloaded examples for swagger and redoc documentation.

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
| /signup | register a user |
| /login | login a user |
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
