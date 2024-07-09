from pydantic import BaseModel, Field
from  typing import Any, Union, Generic, TypeVar

T = TypeVar('T')

class BaseRes(BaseModel, Generic[T]):
    code: int
    msg: str
    data: T
    total: int = 0
    

class Common(BaseModel):
    createTime: Union[str, None] = None
    updateTime: Union[str, None] = None

class IDReq(BaseModel):
    id: Union[int]  = Field(  min=1, description="id必传", example="1")
    

# 定义user
class User(Common):
    name: Union[str] = Field(min_length=1, max_length=100, pattern=".+", description="填写姓名", example="张三")
    # 带 default 则为非必传
    status: Union[int] = Field(default=1, min=1, max=2, description="状态", example="1 , 2")
   
    class Config:
        orm_mode = True
        
class UserUpdate(User):
    id: Union[int]  = Field(  min=1, description="id必传", example="1")
    
    class Config:
        orm_mode = True