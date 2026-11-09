from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    msg = "this is home page"
    return {
        "message": msg
    }

@app.get("/about")
def about():
    msg = "this is about page"
    return {
        "message": msg
    }

@app.get("/contact")
def contact():
    msg = "this is contact page"
    return {
        "message": msg
    }

