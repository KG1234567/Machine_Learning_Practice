# Python version required : 3.10 or newer
# pip install fastapi uvicorn
# python 02_fastapi.py
# uvicorn 02_fastapi:app --reload --port 8000
# https://localhost:8000/docs

from fastapi import FastAPI, HTTPException

app = FastAPI()    # app is central object of a fastapi

FAKE_ITEMS_DB = {
    1: {"name": "keyboard", "price": 49.99},
    2: {"name": "monitor", "price": 199.99},
    3: {"name": "speaker", "price": 74.99},
    4: {"name": "mouse", "price": 87.99},
}


@app.get("/")
def read_root():
    return {"message": "Hello!"}

@app.get("/all_items")
def all_items():
    return FAKE_ITEMS_DB

@app.get("/item/{item_id}")
def all_items(item_id):
    item_id = int(item_id)
    if item_id not in FAKE_ITEMS_DB:
        raise HTTPException(status_code=404, detail="Item not Found")
    else:
        return FAKE_ITEMS_DB[item_id]

# PATH Parameter, with automatic type conversion + validation
@app.get("/itemv2/{item_id}")
def all_items(item_id: int):
    if item_id not in FAKE_ITEMS_DB:
        raise HTTPException(status_code=404, detail="Item not Found")
    else:
        return FAKE_ITEMS_DB[item_id]
    
# Query parameters
@app.get("/search")
def search_items(q: str, limit: int):
    if q is None and limit is None:
        raise HTTPException(status_code=404, detail="Need to pass query parameters")
    else:
        matches = [item for item in FAKE_ITEMS_DB.values() if q.lower() in item["name"]]
        return {"query": q, "limit": limit, "results": matches[:limit]}


# Query parameters, optional with defaults
@app.get("/searchv2")
def search_items(q: str | None = None, limit: int = 10):
    if q is None:
        raise {"query": None, "limit": limit, "results": list(FAKE_ITEMS_DB.values())[:limit]}
    else:
        matches = [item for item in FAKE_ITEMS_DB.values() if q.lower() in item["name"]]
        return {"query": q, "limit": limit, "results": matches[:limit]}

# Post endpoint
@app.post("/items", status_code=201)
def create_item(item : dict):
    new_id = max(FAKE_ITEMS_DB.keys()) + 1
    FAKE_ITEMS_DB[new_id] = item
    return {"id": new_id, **item}

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(app, host="127.0.0.1",port=8000)

