from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  Database_url:str
  Gemini_Api_Key:str

  class Config:
    env_file=".env"

settings=Settings()