from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from sqlalchemy.exc import IntegrityError
from app.database.connection import get_db
from app.database.models import Recipe
from app.schemas import RecipeCreate, RecipeResponse
from sqlalchemy import or_

router = APIRouter()



# API to Create a New Recipe
@router.post("/recipes", response_model=RecipeResponse)
def create_recipe(recipe_in: RecipeCreate, db: Session = Depends(get_db)):
    recipe_data = recipe_in.model_dump(exclude_none=True)
    
    try:
        # it creates a new recipe
        new_recipe = Recipe(**recipe_data)
        
        # it adds to database
        db.add(new_recipe)
        
        db.commit() 
        db.refresh(new_recipe)
        
        return new_recipe
        
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400, 
            detail="Recipe with this name and cuisine already exists"
        )
    except Exception as e:
        db.rollback() 
        raise HTTPException(status_code=400, detail=str(e))



# API to Get All Recipes
@router.get("/recipes", response_model=List[RecipeResponse])
def get_all_recipes(db: Session = Depends(get_db)):
    return db.query(Recipe).all()



# API to Search Recipes
# API to Search Recipes
@router.get("/recipes/search", response_model=List[RecipeResponse])
def search_recipes(
    name: Optional[str] = Query(None),
    ingredients: Optional[List[str]] = Query(None),
    cuisine: Optional[str] = Query(None),
    isVegetarian: bool | None=Query(default=None),
    prepTimeMinutes:Optional[int]=Query(default=None,description="Max Preparation Time in minutes"),
    tags:Optional[str]=Query(None),
    ingredient:Optional[str]=Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Recipe)
    
    # user provided a name it filter by it
    if prepTimeMinutes is not None:
        query=query.filter(or_(Recipe.prepTimeMinutes == prepTimeMinutes,
                                Recipe.prepTimeMinutes <= prepTimeMinutes))
    # else:
    #     query=query.filter(Recipe.prepTimeMinutes<=prepTimeMinutes)
    if name:
        query = query.filter(Recipe.name.ilike(f"%{name}%"))
    if ingredients:
        query = query.filter(Recipe.ingredients.contains(ingredients))
    if cuisine:
        query=query.filter(Recipe.cuisine.contains(cuisine))
    if isVegetarian:
        query=query.filter(Recipe.isVegetarian==isVegetarian)
    if tags:
        query=query.filter(Recipe.tags.contains(tags))
    if ingredient:
        query=query.filter(Recipe.ingredients.contains([ingredient]))
    
    return query.all()



# API to Get a Single Recipe by ID
@router.get("/recipes/{recipe_id}", response_model=RecipeResponse)
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe Not Found"
        )
        
    return recipe
