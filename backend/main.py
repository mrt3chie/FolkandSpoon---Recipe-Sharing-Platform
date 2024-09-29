from fastapi import FastAPI
from routes.recipe_routes import recipe_router

app = FastAPI(title="Recipe API")

# Include recipe-related routes
app.include_router(recipe_router, prefix="/recipes", tags=["Recipes"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Recipe API"}

