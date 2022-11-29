from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from db import Base
from db import ENGINE
from typing import Optional


# モデル定義 
class TestUser(BaseModel):
    id:  Optional[int]
    name: str
    email: str

