from fastapi import FastAPI
from app.routes.recipes import router as recipe_router
from app.routes.ai import router as ai_router
app=FastAPI(title="Smart Recipe Explorer")

app.include_router(recipe_router)
app.include_router(ai_router)