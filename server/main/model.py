from pydantic import BaseModel
from typing import Optional
from datetime import  datetime
from db import AirConditionerModeType

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

#エアコン閾値設定テーブル
class AirConditionerSetting(BaseModel):
    id :Optional[int]
    temperature :int
    mode:Optional[AirConditionerModeType]
    isActive:bool

#エアコン閾値設定更新時
class UpdateAirConditionerSetting(BaseModel):
    temperature:int
    threshold:int
