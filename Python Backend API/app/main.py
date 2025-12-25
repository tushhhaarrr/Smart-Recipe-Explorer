from fastapi import FastAPI
from app.routes import recipes,ai

app=FastAPI(title="Smart Recipe Explorer")

app.include_router(recipes.router,prefix="/recipes",tags=["Recipes"])
app.include_router(ai.router,prefix="/ai",tags=["AI"])

