from pydantic import BaseModel
from typing import Optional
from datetime import  datetime


class CustomBaseModel(BaseModel):
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]

# モデル定義 
class TestUser(CustomBaseModel):
    id:  Optional[int]
    name: str
    email: str

#温度、湿度テーブル
class Thermometer(CustomBaseModel):
    id :Optional[int]
    date :datetime
    temperature:Optional[int]
    humidity:Optional[int]

#大気圧テーブル
class AtmosphericPressure(CustomBaseModel):
    id :Optional[int]
    date :datetime
    pressure:Optional[int]
    altitude:Optional[int]
