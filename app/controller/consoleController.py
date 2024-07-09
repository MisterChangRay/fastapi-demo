from fastapi import APIRouter
from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header



router = APIRouter()


@router.get("/hello")
async def hello():
    """测试函数

    Returns:
        _type_: _description_
    """
    return [{"username": "Rick"}, {"username": "Morty"}]


