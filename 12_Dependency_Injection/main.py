from fastapi import FastAPI, Depends, Header, HTTPException


app = FastAPI()

def common_logic():
    return {"message": "Common logic executed"}


@app.get("/home")
def home(data = Depends(common_logic)):
    return data



def get_current_user():
    return {"user": "tony stark"}

@app.get("/profile")
def profile(user = Depends(get_current_user)):
    return user

@app.get("/about")
def about(user = Depends(get_current_user)):
    return user


# auth part

def verify_token(token: str = Header(None)):
    if token != "secrettoken":
        raise HTTPException(
            status_code = 401,
            detail = "unauthorized"
        )
    return {
        "user": "authorized user"
    }

@app.get("/secure-data")
def secure_data(user = Depends(verify_token)):
    return {
        "message": "secure data access granted",
        "user": user
    }


