# python3 -m venv .venv
# source .venv/bin/activate

from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def get_result():
    return "Welcome to Fastapi"

@app.get('/home')
def get_result():
    return "Welcome to the home page"

@app.get('/home/{name}')
def get_result(name):
    return f"Welcome to Fastapi {name}"

nameOfThings = {
    "city": ["ibadan", "ikeja"],
    "state": ["oyo", "Lagos"],
    "car": ["bmw", "toyota"]
}

listOfLang= {
    1: "python",
    2: "javascript",
    3: "java"
}

@app.get('/home/get_things_name/{name}')
def get_result(name):
    return nameOfThings.get(name, "not vailable")

@app.get('/home/get_num/{num}')
def get_result(num: int):
    return listOfLang.get(num, "not vailable")