from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from sqlalchemy import any_
from typing import List

from app.database import get_db
from app.models import Recipe
from app.schemas import SmartRecipieCreate,RecipieResponse


router=APIRouter()


@router.post("/",response_model=RecipieResponse)
def create_recipe(recipe:SmartRecipieCreate,db:Session=Depends(get_db)):
    new_recipe=Recipe(**Recipe.dic())
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe

@router.get("/",response_model=List[RecipieResponse])
def get_all_recipes(db:Session=Depends(get_db)):
    return db.query(Recipe).all()


@router.get("/{recipe_id}",response_model=RecipieResponse)
def get_recipe(recipe_id:str,db:Session=Depends(get_db)):
    recipe=db.query(Recipe).filter(Recipe.id==recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Recipe Not Found")
    return recipe


@router.get("/filter/search",response_model=List[RecipieResponse])
def filter_recipes(
    cuisine:str |None=None,
    vegeterian:str |None=None,
    maxPrep:int|None=None,
    tag:str|None=None,
    ingredient:str|None=None,
    db:Session=Depends(get_db)


):
    query=db.query(Recipe)

    if cuisine:
        query=query.filter(Recipe.cuisine.ilike(cuisine))
    if vegeterian:
        query=query.filter(Recipe.isVegiterian==vegeterian)
    if maxPrep:
        query=query.filter(Recipe.prepTimeMinutes<=maxPrep)
    if tag:
        query=query.filter(any_(Recipe.tags)==tag)
    if ingredient:
        query=query.filter(any_(Recipe.ingredients)==ingredient)


    return query.all()