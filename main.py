from fastapi import FastAPI
from app.models.model import predict
from pydantic import BaseModel
from app.models.model import __version__

app = FastAPI()

class PredictionInput(BaseModel):
    user_id: int
    song_id: int

@app.get("/")
def home():
    return {"health_check": "OK", "model_version": __version__}

@app.post("/predict")
def get_predict(payload: PredictionInput):
    result = predict(payload.user_id, payload.song_id)
    return result