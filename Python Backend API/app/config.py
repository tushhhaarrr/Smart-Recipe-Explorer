from pydantic import BaseSettings

class Settings(BaseSettings):
  Databse_url:str
  Gemini_Api_Key:str

  class Config:
    env_file=".env"

settings=Settings()