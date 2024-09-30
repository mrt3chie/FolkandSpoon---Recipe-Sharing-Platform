from pydantic import BaseModel
from datetime import datetime

class Recipe(BaseModel):
    name: str
    recipe_id: int
    image: str  
    ingredients: str
    servings: str
    instructions: str  
    createdAt: datetime
    userid: int  

