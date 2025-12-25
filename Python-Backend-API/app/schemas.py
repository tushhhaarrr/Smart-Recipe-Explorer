from pydantic import BaseModel
from typing import List


class SmartRecipieCreate(BaseModel):
    name:str
    cuisine:str
    isVegiterian:bool
    prepTimneMinutes:int
    ingredients:List[str]
    difficulty:str
    instruction:str
    tags:List[str]

class RecipieResponse((SmartRecipieCreate)):
    id:str
    class Config:
        orm_mode=True
        