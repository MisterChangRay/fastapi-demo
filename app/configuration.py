from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str
    mysql_url: str
    app_version: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    
    
    
