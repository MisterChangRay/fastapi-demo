from pydantic import BaseModel
from  typing import Any


class BaseRes(BaseModel):
    code: int
    msg: str
    data: Any