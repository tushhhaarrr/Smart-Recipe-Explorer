import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("Gemini_Api_Key"))

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_recipe_suggestion(ingredients: list[str]) -> str:
    """
    Sends a prompt to Gemini to suggest a recipe based on ingredients.
    """
    ingredients_str = ", ".join(ingredients)
    prompt = f"Suggest a simple recipe using these ingredients: {ingredients_str}. Give short steps."
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise Exception(f"GenAI Error: {str(e)}")

def generate_simplification(instructions: str) -> str:
    """
    Sends a prompt to Gemini to simplify complex recipe instructions.
    """
    prompt = f"Simplify the following recipe instructions for a beginner:\n\n{instructions}"
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise Exception(f"GenAI Error: {str(e)}")
