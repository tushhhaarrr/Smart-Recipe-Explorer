from fastapi import FastAPI
from app.api.recipes import router as recipe_router
from app.api.ai import router as ai_router
from app.database.connection import engine, Base
from app.database import models


# Creating database tables
Base.metadata.create_all(bind=engine)

app=FastAPI(title="Smart Recipe Explorer")

app.include_router(recipe_router)
app.include_router(ai_router)