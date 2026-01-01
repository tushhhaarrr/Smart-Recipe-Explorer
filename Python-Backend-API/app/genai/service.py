from google import genai
import os

client = genai.Client(api_key=os.getenv("Gemini_Api_Key"))

def generate_recipe_suggestion(ingredients: list[str]) -> str:
    """
    Sends a prompt to Gemini to suggest a recipe based on ingredients.
    """
    ingredients_str = ", ".join(ingredients)
    prompt = f"Suggest a simple recipe using these ingredients: {ingredients_str}. Give short steps."
    
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        raise Exception(f"GenAI Error: {str(e)}")

def generate_simplification(instructions: str) -> str:
    """
    Sends a prompt to Gemini to simplify complex recipe instructions.
    """
    prompt = f"""Simplify the following recipe instructions for a beginner:\n\n{instructions}and You're a food_only ai Assistant. you must answer questions related to food only and do not give 
    Do NOT answer non-food questions.
Do NOT provide explanations, code, general knowledge, or advice unrelated to food.
Do NOT mention that you are an AI or explain your limitations.

Stay strictly within the food domain at all times.
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        raise Exception(f"GenAI Error: {str(e)}")
