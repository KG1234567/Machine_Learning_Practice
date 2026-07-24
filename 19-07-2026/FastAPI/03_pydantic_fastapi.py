# Python version required : 3.10 or newer
# pip install fastapi uvicorn
# python 02_fastapi.py
# uvicorn 02_fastapi:app --reload --port 8000
# https://localhost:8000/docs

## Validation requests bodies with pydantic

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()    # app is central object of a fastapi


class Item(BaseModel):
    name: str = "None"
    price: float = 0

FAKE_ITEMS_DB = {
    1: {"name": "keyboard", "price": 49.99},
    2: {"name": "monitor", "price": 199.99},
    3: {"name": "speaker", "price": 74.99},
    4: {"name": "mouse", "price": 87.99},
}

@app.get("/searchv2")
def search_items(q: str | None = None, limit: int = 10):
    if q is None:
        raise {"query": None, "limit": limit, "results": list(FAKE_ITEMS_DB.values())[:limit]}
    else:
        matches = [item for item in FAKE_ITEMS_DB.values() if q.lower() in item["name"]]
        return {"query": q, "limit": limit, "results": matches[:limit]}

@app.post("/items", status_code=201)
def create_item(item : Item):
    new_id = max(FAKE_ITEMS_DB.keys()) + 1
    input_ = {"name": item.name, "price": item.price}
    FAKE_ITEMS_DB[new_id] = input_
    return {"id": new_id, **input_}

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(app, host="127.0.0.1",port=8000)

