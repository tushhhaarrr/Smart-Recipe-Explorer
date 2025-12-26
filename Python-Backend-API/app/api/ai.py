from fastapi import APIRouter, HTTPException, status, Depends
from typing import List, Dict
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.database.models import AISuggestion
from app.genai import service 
from app.schemas import SimplifyRequest 

# router for ai
router = APIRouter()



# API to Suggest a Recipe based on Ingredients
@router.post("/ai/suggest")
def suggest_recipe(ingredients: List[str], db: Session = Depends(get_db)):
    """
    This function takes a list of ingredients and asks the AI to 
    suggest a good recipe we can make with them.
    """

    if not ingredients:
        raise HTTPException(status_code=400, detail="Please provide at least one ingredient")
    
    try:
        # Call our service layer to get the content
        suggestion_text = service.generate_recipe_suggestion(ingredients)
        
    except Exception as e:
        # If the AI service fails for some reason
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    
    # I want to save this suggestion to the database so we have a history
    try:
        new_suggestion = AISuggestion(
            ingredients=ingredients,
            suggestion_text=suggestion_text
        )
        db.add(new_suggestion)
        db.commit()
    except Exception as e:
        # If saving to DB fails, I print it to console but I don't stop the user
        print(f"Failed to save to history: {e}") 

    # Return the ingredients and the AI's answer
    return {
        "ingredients": ingredients,
        "suggestion": suggestion_text
    }



# API to Simplify Complex Instructions
@router.post("/ai/simplify")
def simplify_recipe(request_body: SimplifyRequest):
    """
    This function takes hard/long recipe instructions and asks AI 
    to rewrite them in a simple way for beginners.
    """
    
    try:
        simplified_text = service.generate_simplification(request_body.instructions)
        
      
        return {"simplified_instructions": simplified_text}
        
    except Exception as e:
        # Handle crashes nicely
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    
