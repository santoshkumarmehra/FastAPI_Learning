from fastapi import FastAPI, HTTPException, status

app = FastAPI()


#status code
@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(name: str, age: int):
    return {"message": "User created successfully"}


#custom response
@app.get("/users")
def get_user():
    return {
        "name": "sam",
        "age": 25,
    }


#error handling
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id != 1:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User not found"
        )
    return {
        "id":1,
        "name": "shanon"
    }






