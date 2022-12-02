from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import Column, Integer, String, DateTime
import datetime as dt 
import os
from core.config import PROJECT_ROOT
from dotenv import load_dotenv

load_dotenv(verbose=True)
print(PROJECT_ROOT)
load_dotenv(dotenv_path=os.path.join(PROJECT_ROOT, '.env'))
DATABASE_URL = ""

if("main" in PROJECT_ROOT ):
    DATABASE_URL = os.environ.get('BATCH_DATABASE_URL')
else:
    DATABASE_URL = os.environ.get('DATABASE_URL')
    
print("DATABASE_URL:",DATABASE_URL)
ENGINE = create_engine(
    DATABASE_URL,
    encoding="utf-8",
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()



# テーブル定義
class TestUserTable(Base):
    __tablename__ = 'test_user_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=True)
    # email = Column(String(128), nullable=False)
    # createdAt = Column(DateTime, nullable=False,default=12)
    # updatedAt = Column(DateTime, nullable=False,onupdate=dt.datetime.now)

#温度、湿度テーブル
class ThermometerTable(Base):
    __tablename__ = 'thermometer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, nullable=False)
    temperature = Column(Integer, nullable=True)
    humidity = Column(Integer, nullable=True)
    createdAt = Column(DateTime, nullable=False,default=dt.datetime.now)
    updatedAt = Column(DateTime, nullable=False,default=dt.datetime.now,onupdate=dt.datetime.now)
