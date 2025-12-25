from fastapi import APIRouter,HTTPException,status
import google.generativeai as genai
import os
from dotenv import load_dotenv
from app.database import get_db
from app.models import AIsuggestion

load_dotenv()

genai.configure(api_key=os.getenv("Gemini_Api_Key"))

model=genai.GenerativeModel("gemini-2.5-flash")
router=APIRouter()

@router.post("/ai/suggest")
def suggest_recipe(ingredients:list[str]):
    prompt=(
          "Suggest a simple recipe using these ingredients:\n"
        + ", ".join(ingredients)
        + "\nGive short steps."
    )
    try:
     response=model.generate_content(prompt)
     suggestion_text=response.text
    except Exception:
      raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Ai service is unavailable")
    
    db=next(get_db())
    ai_record=AIsuggestion(
      ingredients=ingredients,
      suggestion_text=suggestion_text
    )
    db.add(ai_record)
    db.commit()
    return{
      "ingredients":ingredients,
      "suggestion":suggestion_text
    }


@router.post("/ai/simplify")
def simplify_recipe(instructions:str):
    Prompt=(
        "Simplify the following recipe instructions"
        "for a beginner:\n\n"+instructions
    )
    try:
     response=model.generate_content(Prompt)
     return{"simplified_instructions":response.text}
    except Exception:
      raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="AI Service is currently unavailable"
            )
    
