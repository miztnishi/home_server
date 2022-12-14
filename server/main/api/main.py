from typing import Union
from fastapi import FastAPI
from db import AirConditionerModeType, session  ,ThermometerTable, AirConditionerSettingTable
from model import  AirConditionerSetting, Thermometer, UpdateAirConditionerSetting
import datetime as dt 
import sys
import os
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/util")
from fastapi.middleware.cors import CORSMiddleware
from air_con_util import air_con_util

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



#　ユーザー情報一覧取得
@app.get("/")
def get():
    return {"test":"test"}


# #　thermometer情報一覧取得
# @app.get("/thermometer")
# def get_thermometer_list():
#     thermometers = session.query(ThermometerTable).all()
#     return thermometers


# thermometer情報取得(日付指定)
@app.get("/thermometer")
def get_user(start: str = None,end:str=None):
    start = dt.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
    end = dt.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
    print(start)
    print(end)
    thermometer = session.query(ThermometerTable).\
        filter(ThermometerTable.date.between(start,end)).all()
    return thermometer


# thermometer情報登録
@app.post("/thermometer")
def post_user(thermometer: Thermometer):
    thermometer = ThermometerTable(date=thermometer.date
                                    ,temperature=thermometer.temperature
                                    ,humidity=thermometer.humidity)
    session.add(thermometer)    
    session.commit()
    return thermometer


#　エアコン閾値設定情報一覧取得
@app.get("/airConditionerSetting")
def get_air_conditioner_setting_list():
    setting = session.query(AirConditionerSettingTable).all()
    return setting


#　エアコン閾値設定情報更新
@app.patch("/airConditionerSetting/{mode}" )
def update_air_conditioner_setting(mode:AirConditionerModeType ,data:UpdateAirConditionerSetting):
    setting:AirConditionerSettingTable 
    setting = session.query(AirConditionerSettingTable).filter(AirConditionerSettingTable.mode==mode).first() 
    if(not setting):
        return
    setting.temperature = data.temperature
    setting.threshold = data.threshold
    setting.isActive = True
    #他のモードの稼働状況をOFFに変更
    settings = session.query(AirConditionerSettingTable).filter(AirConditionerSettingTable.mode != mode).all()
    map = []
    for setting in settings:
        map.append({"id":setting.id ,"isActive":False })
    session.bulk_update_mappings(AirConditionerSettingTable, map )
    session.commit()
    
#　エアコン閾値設定情報更新 稼働状況をOFFに変更
@app.post("/airConditionerSetting/non-active" )
def update_air_conditioner_setting_to_non_active():
    settings = session.query(AirConditionerSettingTable).all()
    map = []
    for setting in settings:
        map.append({"id":setting.id ,"isActive":False })
    session.bulk_update_mappings(AirConditionerSettingTable, map )
    session.commit()
    

#　エアコンに信号を送る
@app.post("/airConditioner/send-signal" )
def send_signal_to_air_conditioner():
    air_con = air_con_util()
    #一度電源を落とす
    res = air_con.send_signal("Aircon_OFF") 
    time.sleep(2)
    settings:AirConditionerSettingTable = session.query(AirConditionerSettingTable).filter(AirConditionerSettingTable.isActive == True ).first()
    #電源をつける
    res = air_con.send_signal("Aircon_ON") 
    time.sleep(2)
    print(f"Aircon_mode_{settings.mode}")
    #運転モードを変更
    air_con.send_signal(f"Aircon_mode_{settings.mode}")
    time.sleep(2)
    #温度設定
    print(f"Aircon_mode_{settings.mode}_{settings.temperature}")
    air_con.send_signal(f"Aircon_mode_{settings.mode}_{settings.temperature}")
    return res

#　エアコンに信号を送る
@app.post("/airConditioner/send-signal/off" )
def send_signal_to_air_conditioner_off():
    air_con = air_con_util()
    #電源を落とす
    res = air_con.send_signal("Aircon_OFF") 

