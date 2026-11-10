from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


## Pydantic model data validation with nested schema
# nested schema
# http://127.0.0.1:8000/create-user
#input
# {
#   "name": "sunny",
#   "age": 29,
#   "adddress": {
#     "city": "bhopal",
#     "pincode": 201012
#   }
# }

# output
# {
#   "message": "User created successfully",
#   "user": {
#     "name": "sunny",
#     "age": 29,
#     "adddress": {
#       "city": "bhopal",
#       "pincode": 201012
#     }
#   }
# }


class Address(BaseModel):
    city: str
    pincode: int
    

class User(BaseModel):
    name: str
    age: int
    adddress: Address


@app.post("/create-user")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "user": user
    }





