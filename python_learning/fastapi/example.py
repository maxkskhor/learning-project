from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"Data": "Testing"}


@app.get("/about")
def about():
    return {"Data": "About"}

# http://127.0.0.1:8000/docs gives the FastAPI interface
