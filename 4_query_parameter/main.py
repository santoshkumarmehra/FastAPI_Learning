from fastapi import FastAPI

app = FastAPI()

# query parameter
# without any option , this is a required query parameter
# http://127.0.0.1:8000/users?name=santosh

@app.get("/users")
def users(name):
    return {
        "name": name
    }


# optional query parameter
# http://127.0.0.1:8000/users?name=santosh // santosh
# http://127.0.0.1:8000/users //None

@app.get("/users_optional")
def users_optional(name: str = None):
    return {
        "name": name
    }

# default query parameter
# http://127.0.0.1:8000/product?limit=200 //200
# http://127.0.0.1:8000/product //10

@app.get("/product")
def product(limit: int = 10):
    return {
        "limit": limit
    }


# multiple query parameter
# http://127.0.0.1:8000/items?name=laptop&price=2000 // {
#   "name": "laptop",
#   "price": 2000
# }
# http://127.0.0.1:8000/items // 
# {
#   "name": null,
#   "price": 0
# }

@app.get("/items")
def items(name: str = None, price: int = 0):
    items = {
        "name": name,
        "price": price
    }
    return items




