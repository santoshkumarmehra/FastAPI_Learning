from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



# http://127.0.0.1:8000/create-user?name=rahul&age=23
# {
#   "name": "rahul",
#   "age": 23
# }

@app.post("/create-user-trial")
def create_user_trial(name: str, age: int):
    return {"name": name, "age": age}


# without pydantic model, we can use dict to accept the request body
#http://127.0.0.1:8000/create-user
#input 
# # {
#   "name": "santosh",
#   "age": 110,
#   "class": "standard"
# }
#o/p
# {
#   "message": "User created successfully",
#   "user": {
#     "name": "santosh",
#     "age": 110,
#     "class": "standard"
#   }
# }

@app.post("/create-user-without-pydantic")
def create_user_without_pydantic(user: dict):
    return {
        "message": "User created successfully",
        "user": user
    }



# with pydantic model, we can use pydantic model to accept the request body
#http://127.0.0.1:8000/create-user-with-pydantic
#input
# {
#   "name": "sohan",
#   "age": 19,
#   "class_": "12th",
#   "roll_number": 6
# }
#o/p
# {
#   "message": "User created successfully",
#   "user": {
#     "name": "sohan",
#     "age": 19,
#     "class_": "12th",
#     "roll_number": 6
#   }
# }

class User(BaseModel):
    name: str
    age: int
    class_: str
    roll_number: int

@app.post("/create-user-with-pydantic")
def create_user_with_pydantic(user: User):
    return {
        "message": "User created successfully",
        "user": user
    }



