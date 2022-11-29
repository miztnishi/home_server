from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import Column, Integer, String
import os
from core.config import PROJECT_ROOT
from dotenv import load_dotenv

load_dotenv(verbose=True)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(dotenv_path=os.path.join(PROJECT_ROOT, '.env'))

DATABASE_URL = os.environ.get('DATABASE_URL') 
print(DATABASE_URL)

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
    name = Column(String(30), nullable=False)
    email = Column(String(128), nullable=False)

