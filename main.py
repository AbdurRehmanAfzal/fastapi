from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open("patients.json") as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {"message": "Patient management system!"}

@app.get("/about")
def about():
    return {"message": "This is a FastAPI application."}

@app.get("/patients")
def get_patients():
    data = load_data()
    return data