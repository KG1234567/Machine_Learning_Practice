# Python version required : 3.10 or newer
# pip install fastapi uvicorn
# python 01_fastapi.py
# uvicorn 01_fastapi:app --reload --port 8000

from fastapi import FastAPI 

app = FastAPI()    # app is central object of a fastapi


# route (also called as endpoint or path operation)
@app.get("/")
def read_root():
    return {"message": "Hello!"}

@app.get("/say_hello")
def say_hello_python():
    return {"message": "Hello from us"}

@app.get("/say_hello/{name}")
def say_hello_python(name: str):
    return {"message": f"Hello {name}"}

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(app, host="127.0.0.1",port=8000)

