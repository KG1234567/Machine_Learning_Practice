from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="IRIS CLASSIFIER APP")


def iris_model(a,b,c,d):
    return "setosa"

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class PredictionResponse(BaseModel):
    predicted_species: str
    confidence: float

@app.post("/predict", response_model=PredictionResponse)
def predict_iris(features: IrisFeatures):
    response = iris_model(features.sepal_length, features.sepal_width, features.petal_length, features.petal_width)
    return PredictionResponse(
        predicted_species=response[0],
        confidence=response[1]
    )


if __name__ == "__main__":

    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)


