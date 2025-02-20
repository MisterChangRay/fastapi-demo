from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime, update
from sqlalchemy.pool import QueuePool
from ..configuration import get_settings

SQLALCHEMY_DATABASE_URL = get_settings().mysql_url

# echo 参数用于打印sql
engine = create_engine(
    url=SQLALCHEMY_DATABASE_URL
    , poolclass=QueuePool
    , pool_size=20
    , max_overflow=0
    , echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


# t_user 表结构定义
class TUser(Base):
    __tablename__ = "t_user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(Integer)
    create_time = Column(DateTime)
    update_time = Column(DateTime)
    

# t_keyvalue 表结构定义
class TKeyValue(Base):
    __tablename__ = "t_keyvalue"

    key = Column(String, primary_key=True)
    value = Column(Integer)
    create_time = Column(DateTime)
    update_time = Column(DateTime)
    expire_time = Column(DateTime)
    