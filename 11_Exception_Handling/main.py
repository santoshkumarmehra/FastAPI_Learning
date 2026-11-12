from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import JSONResponse


app = FastAPI()


class UserNotFoundException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(UserNotFoundException)
def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
                "status": "error",
                "message": f"User with name {exc.name} not found."
            },
    )


@app.get("/users/{name}")
def get_user(name: str):
    if name != "sam":
        raise UserNotFoundException(name=name)
    return {"name": name}


