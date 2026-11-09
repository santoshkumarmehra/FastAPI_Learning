from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{id}")
def users_id(id: int):
    return {
        "users_id": id
    }



