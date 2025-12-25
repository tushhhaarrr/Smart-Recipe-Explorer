from pydantic import BaseModel
from typing import List, Optional

class RecipeCreate(BaseModel):
    name: str
    cuisine: str
    isVegetarian: bool
    prepTimeMinutes: int
    ingredients: List[str]
    difficulty: str
    instructions: str
    tags: List[str]
    description: str

class RecipeResponse(RecipeCreate):
    id: int

    class Config:
        from_attributes = True

class RecipeSearch(BaseModel):
    name: Optional[str] = None
    ingredients: Optional[List[str]] = None
        