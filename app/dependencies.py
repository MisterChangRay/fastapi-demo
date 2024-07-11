from typing import Annotated
from fastapi import Header, HTTPException
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from .configuration import Settings
from .orm import schemas
from .orm.schemas import SessionLocal
import datetime
from sqlalchemy.orm import Session

async def get_token_header(token: str = Header()):
    """全局session校验入口
    可以在这里校验header中的sessionkey

    Args:
        token (str, optional): _description_. Defaults to Header().

    Raises:
        HTTPException: _description_
    """
    if token  != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="XToken header invalid")







# Dependency
def get_db(request: Request):
    """全局获取注入数据库

    Args:
        request (Request): _description_

    Returns:
        _type_: _description_
    """
    return request.state.db



