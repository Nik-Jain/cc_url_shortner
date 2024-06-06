from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    env_name:str = 'LOCAL'
    base_url:str = 'http://localhost:8000'
    db_url:str = 'sqlite:///./shortner.db'
    
    class Config:
        env_file = ".env"        

@lru_cache
def get_settings():
    setting = Settings()
    print(f'Loading settings for: {setting.env_name}')
    return setting

