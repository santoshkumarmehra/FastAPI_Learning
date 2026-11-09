from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    msg = "this is a fast api"
    return {
        "message": msg
    }
    

