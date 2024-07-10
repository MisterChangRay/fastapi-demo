from pydantic import BaseModel, Field
from  typing import Any, Union, Generic, TypeVar

T = TypeVar('T')

# 基本返回对象
class BaseRes(BaseModel, Generic[T]):
    code: int
    msg: Union[str, None] = "okk"
    data: Union[T, None] = None
    total: int = 0
    

# 公共
class Common(BaseModel):
    createTime: Union[str, None] = None
    updateTime: Union[str, None] = None


# 简单id请求
class IDReq(BaseModel):
    id: Union[int]  = Field(  min=1, description="id必传", example="1")
    

# 定义user
class User(Common):
    name: Union[str] = Field(min_length=1, max_length=100, pattern=".+", description="填写姓名", example="张三")
    # 有 default 定义则为非必传
    status: Union[int] = Field(default=1, min=1, max=2, description="状态", example="1 , 2")
   
    class Config:
        from_attributes = True

# user更新实体        
class UserUpdate(User):
    id: Union[int]  = Field(  min=1, description="id必传", example="1")
    
    class Config:
        from_attributes = True