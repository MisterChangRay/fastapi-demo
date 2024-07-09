from fastapi import APIRouter
from fastapi import APIRouter, Depends, HTTPException,Body
from sqlalchemy.orm import Session
from ..dependencies import get_db
from .models import models
from ..orm import schemas
from loguru import logger
from pydantic import BaseModel
from typing import List,Annotated
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime, update, delete
router = APIRouter()



    
@router.post("/add")
async def adduser(user: Annotated[models.User, Body(embed=True)],  db: Session = Depends(get_db)) -> models.BaseRes:
    """
    用户列表
    json方式获取数据
    Returns:
        _type_: _description_
    """
    
    user = schemas.TUser(name=user.name, status=user.status, create_time=user.createTime, update_time=user.updateTime)
    db.add(user)
    db.commit()
    return models.BaseRes(code=0, msg="okk")



@router.get("/", response_model=List[models.User])
async def listuser( db: Session = Depends(get_db)) :
    """
    用户列表, 包含分页

    Returns:
        _type_: _description_
    """
    
    res =  db.query(schemas.TUser).offset(2).limit(10).all()
    return res



@router.get("/{id}", response_model=models.BaseRes[ models.User])
async def getuser(id: int, db: Session = Depends(get_db)) :
    """
    根据id获取用户

    Returns:
        _type_: _description_
    """
    
    res =  db.query(schemas.TUser).where(schemas.TUser.id == id).limit(1).first()
    return models.BaseRes(code=0, msg="okk", data=res)



@router.put("/", response_model=models.BaseRes )
async def updateuser(user: Annotated[models.UserUpdate, Body(embed=True)], db: Session = Depends(get_db)) -> models.BaseRes:
    """
    根据id更新用户

    Returns:
        _type_: _description_
    """
 
    
    updatesql = update(schemas.TUser).values(name=user.name, status=user.status).where(schemas.TUser.id == user.id)
    db.execute(updatesql)
    db.commit()
    return models.BaseRes(code=0, msg="okk")




@router.delete("/{id}")
async def deleteuser(id:int, db: Session = Depends(get_db)) -> models.BaseRes:
    """
    根据id删除用户

    Returns:
        _type_: _description_
    """
    deletesql = delete(schemas.TUser).where(schemas.TUser.id == id)
    db.execute(deletesql)
    db.commit()
    return models.BaseRes(code=0, msg="okk")





@router.post("/transaction/{id}")
async def transactionDemo(id:int, db: Session = Depends(get_db)) -> models.BaseRes:
    """
    修改状态，事务演示
    获取连接时，已经代理session。 此时只需要在方法中控制事务即可

    Returns:
        _type_: _description_
    """
    try:
        deletesql = delete(schemas.TUser).where(schemas.TUser.id == id)
        db.execute(deletesql)
    except Exception as ae:
        # 异常发生执行代码,
        db.rollback()
        logger.error(ae)
    else:
        # 异常没发生执行的代码
        db.commit()
    finally:
        #异常发生不发生都要执行代码
        pass
        
    return models.BaseRes(code=0, msg="okk")