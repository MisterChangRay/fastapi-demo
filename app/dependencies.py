from typing import Annotated
from functools import lru_cache
from fastapi import Header, HTTPException
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from .configuration import Settings

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


@lru_cache
def get_settings():
    return Settings()





# Dependency
def get_db(request: Request):
    """全局获取注入数据库

    Args:
        request (Request): _description_

    Returns:
        _type_: _description_
    """
    return request.state.db