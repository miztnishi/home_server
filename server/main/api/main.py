from fastapi import FastAPI
from db import session ,TestUserTable ,ThermometerTable
from model import  Thermometer
import datetime as dt 
app = FastAPI()

#　ユーザー情報一覧取得
@app.get("/")
def get():
    return {"test":"test"}


#　thermometer情報一覧取得
@app.get("/thermometer")
def get_thermometer_list():
    thermometers = session.query(ThermometerTable).all()
    return thermometers


# thermometer情報取得(日付指定)
@app.get("/thermometer")
def get_user(start: str = None,end:str=None):
    start = dt.datetime.date(start)
    end = dt.datetime.date(end)
    thermometer = session.query(ThermometerTable).\
        filter(ThermometerTable.date.between(start,end)).first()
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

# # ユーザ情報更新
# @app.put("/test_users/{user_id}")
# def put_users(user: TestUser, user_id: int):
#     target_user = session.query(TestUserTable).\
#         filter(TestUserTable.id == user_id).first()
#     target_user.name = user.name
#     target_user.email = user.email
#     session.commit()


