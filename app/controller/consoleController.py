from fastapi import APIRouter
from fastapi import APIRouter, Depends, HTTPException
from loguru import logger
from ..dependencies import get_token_header
from ..configuration import Settings
from .models import models

from ..service import KVService

router = APIRouter()


@router.get("/hello")
async def hello():
    """测试函数

    Returns:
        _type_: _description_
    """
    return [{"username": "Rick"}, {"username": "Morty"}]




@router.get("/kvtest/{type}", response_model=models.BaseRes)
async def kvtest(type:int):
    """测试kvservice

    Returns:
        _type_: _description_
    """
    
    if(type == 1):
        KVService.set(key="123", value="456", ttl=60)
        return models.BaseRes(code=0,msg="okk")
    if(type == 2):
        res = KVService.getValue("123")
        return models.BaseRes(code=0,msg="okk", data=res)
    if(type == 3):
        res = KVService.getAndDelete("123")
        return models.BaseRes(code=0,msg="okk", data=res)
        
    return models.BaseRes(code=0,msg="invalid")


