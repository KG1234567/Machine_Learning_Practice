# Python version required : 3.10 or newer
# pip install fastapi uvicorn

from fastapi import FastAPI 

app = FastAPI()    # app is central object of a fastapi


# route (also called as endpoint or path operation)
@app.get("/")
def read_root():
    return {"message": "Hello!"}

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(app, host="127.0.0.1",port=8000)

