# Python version required : 3.10 or newer
# pip install fastapi uvicorn
# python 02_fastapi.py
# uvicorn 02_fastapi:app --reload --port 8000
# https://localhost:8000/docs

from fastapi import FastAPI 

app = FastAPI()    # app is central object of a fastapi

FAKE_ITEMS_DB = {
    1: {"name": "keyboard", "price": 49.99},
    2: {"name": "monitor", "price": 199.99},
}


@app.get("/")
def read_root():
    return {"message": "Hello!"}

@app.get("/all_items")
def all_items():
    return FAKE_ITEMS_DB

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(app, host="127.0.0.1",port=8000)

