import uuid
from sqlalchemy import Column,Integer,String,Boolean,ARRAY
from app.database import Base

class Recipe(Base):
    __tablename__="recipes"

    id=Column(String,primary_key=True,default=lambda:str(uuid.uuid4()))
    name=Column(String,nullable=False)
    cuisine=Column(String,nullable=False)
    isVegiterian=Column(Boolean,default=True)
    prepTimeMinutes=Column(Integer,nullable=False)
    ingredients=Column(ARRAY(String),nullable=False)
    tags=Column(ARRAY(String),nullable=False)

    