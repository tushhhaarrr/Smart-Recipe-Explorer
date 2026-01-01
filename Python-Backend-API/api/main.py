from fastapi import FastAPI
from app.api.recipes import router as recipe_router
from app.api.ai import router as ai_router

app = FastAPI(
    title="Smart Recipe Explorer",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"status": "ok"}

app.include_router(recipe_router, prefix="/recipes", tags=["Recipes"])
app.include_router(ai_router, prefix="/ai", tags=["AI"])