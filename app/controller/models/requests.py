from pydantic import BaseModel
from typing import Union

class User(BaseModel):
    id: Union[int, None] = None
    name: Union[str, None] = None
    status: Union[int, None] = None
    createTime: Union[str, None] = None
    updateTime: Union[str, None] = None