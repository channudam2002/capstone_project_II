from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
# from app.models.model import predict
# from app.models.model import __version__

app = FastAPI()

# class PredictionInput(BaseModel):
#     user_id: int
#     song_id: int

# @app.get("/")
# def home():
#     return {"health_check": "OK", "model_version": __version__}

# @app.post("/predict")
# def get_predict(payload: PredictionInput):
#     result = predict(payload.user_id, payload.song_id)
#     return result

class CreateUser(BaseModel):
    user_id: int
    user_name: str
    user_gender: str
    user_age: int
    user_city: str
    status: Optional[bool] = True

# request query
@app.get("/users")
def get_users(total: int, location:str="Phnom Penh", age: Optional[str] = None):
    return {"data": f"fetch {total} users which are living in {location} from database"}

# request params
@app.get("/users/{id}")
def get_user_by_id(id: int):
    return {"data": f"fetch user with id: {id}"}

#request body
@app.post("/users")
def create_user(user: CreateUser):
    return {"data": {
        "id": user.user_id,
        "name": user.user_name,
        "gender": user.user_gender,
        "status": user.status
    }}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    