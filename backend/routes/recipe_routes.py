from fastapi import APIRouter, HTTPException
from typing import List, Union
from models.model import Recipe
from service.recipe_services import ( 
    create_recipe_service,
    get_recipe_service,
    get_all_recipe_service,
    update_recipe_service,
    delete_recipe_service

)

recipe_router = APIRouter()

@recipe_router.post("/", response_model=dict)
def create_recipe(recipe: Recipe):
    result = create_recipe_service(recipe)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result)
    return result

@recipe_router.get("/", response_model=Union[dict, List[Recipe]])
def get_recipe(recipe_id: int):
    result = get_recipe_service(recipe_id)
    if isinstance(result, dict) and "message" in result:
        raise HTTPException(status_code=404, detail=result["message"])
    return result

@recipe_router.get("/all", response_model=Union[dict, List[Recipe]])
def get_all_recipe():
    result = get_all_recipe_service()
    if isinstance(result, dict) and "message" in result:
        raise HTTPException(status_code=404, detail=result["message"])
    return result

@recipe_router.put("/{recipe_id}", response_model=dict)
def update_recipe(recipe_id: int, updated_fields: dict):
    result = update_recipe_service(recipe_id, updated_fields)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result)
    return result

@recipe_router.delete("/{recipe_id}", response_model=dict)
def delete_recipe(recipe_id: str):
    result = delete_recipe_service(recipe_id)
    if "message" in result and "failed" in result["message"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result
