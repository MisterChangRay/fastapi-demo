from fastapi import APIRouter
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from .models.requests import User
from .models.rseponse import BaseRes

from ..orm.models import TUser
from pydantic import BaseModel
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime, update
router = APIRouter()



    
@router.post("/add")
async def userlist(user: User, db: Session = Depends(get_db)) -> BaseRes:
    """
    用户列表

    Returns:
        _type_: _description_
    """
    
    user = TUser(name=user.name, status=user.status, create_time=user.createTime, update_time=user.updateTime)
    db.add(user)
    db.commit()
    return BaseRes(code=0, msg="okk")


