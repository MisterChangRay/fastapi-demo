from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

# 配置文件实体类
# 注意大小写需要保持一致
class Settings(BaseSettings):
    app_name: str
    mysql_url: str
    app_version: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    
    
    
@lru_cache
def get_settings():
    return Settings()
