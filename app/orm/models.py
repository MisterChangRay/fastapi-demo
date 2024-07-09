from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime, update
from sqlalchemy.pool import QueuePool

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:2vKeG&1.3@47.109.108.16:7501/fastapi_demo"


engine = create_engine(
    url=SQLALCHEMY_DATABASE_URL, poolclass=QueuePool
    # , echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
class TUser(Base):
    __tablename__ = "t_user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(Integer)
    create_time = Column(DateTime)
    update_time = Column(DateTime)
    