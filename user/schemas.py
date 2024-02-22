from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    gender: str
    age: int
    city: str
    status: Optional[bool] = True