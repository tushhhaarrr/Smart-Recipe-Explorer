from fastapi import FastAPI
from app.api.recipes import router as recipe_router
from app.api.ai import router as ai_router

app = FastAPI(title="Smart Recipe Explorer")

@app.get("/")
def root():
    return {"status": "ok"}

app.include_router(recipe_router)
app.include_router(ai_router)
