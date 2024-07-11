from typing import Annotated
from functools import lru_cache
from fastapi import Header, HTTPException
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from ..orm import schemas
from ..orm.schemas import SessionLocal
import datetime
from sqlalchemy.orm import Session
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime, update, delete
from sqlalchemy.dialects.mysql import Insert

# 一个简单的,基于mysql实现的keyvalue 保存机制
def set(key:str, value:str, ttl:int=60):
    """基于数据库设置值
        这里同样演示了mysql insert on duplicate 使用

    Args:
        key (str): key
        value (str): value
        ttl (int, optional): 过期时间, 秒. Defaults to 60.

    Returns:
        _type_: _description_
    """
    with SessionLocal() as session:
        create = datetime.datetime.now()
        extime = datetime.datetime.now() +  datetime.timedelta( seconds=ttl )
        
        insertstmt = Insert(schemas.TKeyValue).values(key=key, value= value, create_time=create, update_time=create, expire_time = extime)
        insertstmt = insertstmt.on_duplicate_key_update(value= value, expire_time=extime, update_time=create)
        
        session.execute(insertstmt)
        session.commit()
        return True


def get(key:str):
    """获取key值, 返回对象

    Args:
        key (str): _description_

    Returns:
        _type_: _description_
    """
    with SessionLocal() as session:
        res =  session.query(schemas.TKeyValue).where(schemas.TKeyValue.key == key).limit(1).first()
        if(res is not None and  res.expire_time <= datetime.datetime.now()) :
            return None
        return res


def deleteKey(key:str):
    if(key is None):
        return
    with SessionLocal() as session:
        deletesql = delete(schemas.TKeyValue).where(schemas.TKeyValue.key == key)
        session.execute(deletesql)
        session.commit()


def getValue(key:str):
    res = get(key)
    if(res is None) :
        return None
    else:
        return res.value
    
def getAndDelete(key:str):
    res = get(key)
    if(res is not None) :
        with SessionLocal() as session:
            deletesql = delete(schemas.TKeyValue).where(schemas.TKeyValue.key == res.key)
            session.execute(deletesql)
            session.commit()
        
        return res.value
    else:
        return None
    
    
def expireData():
    """淘汰过期数据
    通过定时任务每分钟执行
    """
    
    with SessionLocal() as session:
        deletesql = delete(schemas.TKeyValue).where(schemas.TKeyValue.expire_time <=  datetime.datetime.now())
        session.execute(deletesql)
        session.commit()
  
  
def expireData_old():
    with SessionLocal() as session:
        res =  session.query(schemas.TKeyValue).where(schemas.TKeyValue.expire_time <= datetime.datetime.now()).limit(10).all()
        ids = []
        for tmp in res :
            ids.append(tmp.key)
        if(len(ids) > 0) :
            deletesql = delete(schemas.TKeyValue).where(schemas.TKeyValue.key in ids)
            session.execute(deletesql)
            session.commit()
  