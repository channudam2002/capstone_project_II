from keras.models import load_model
from pathlib import Path
import numpy as np
import pandas as pd

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

loaded_model = load_model(f"{BASE_DIR}/tensorflow_model.h5")

df = pd.read_csv(f"{BASE_DIR}/kkbox_cleaned_dataset.csv")

def predict(user_id, song_id):
    X = df[(df.msno == user_id) & (df.song_id == song_id)].drop(["Unnamed: 0","target"], axis=1).to_numpy()
    proba = float(list(loaded_model.predict(X).flatten())[0])
    return {"probability": round(proba, 2)}