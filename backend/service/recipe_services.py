from typing import List, Union
from models.model import Recipe
from db.supabase_client import create_supabase_client
from datetime import datetime

supabase = create_supabase_client()

def recipe_exists(key: str, value: Union[str, int]) -> bool:
    response = supabase.from_("recipes").select("*").eq(key, value).execute()
    return len(response.data) > 0

def create_recipe_service(recipe: Recipe) -> dict:
    try:
        if recipe_exists("recipe_id", recipe.recipe_id):
            return {"message": "Recipe already exists"}

        new_recipe = supabase.from_("recipes").insert({
            "name": recipe.name,
            "recipe_id": recipe.recipe_id,
            "image": recipe.image,
            "ingredients": recipe.ingredients,
            "servings": recipe.servings,
            "instructions": recipe.instructions,
            "createdAt": recipe.createdAt.isoformat(),
            "userid": recipe.userid
        }).execute()

        # Check for successful creation
        if new_recipe.data is not None:
            return {"message": "Recipe created successfully", "data": new_recipe.data}
        else:
            # If there is no data, we might want to check for an error message instead
            return {"message": "Recipe creation failed", "error": str(new_recipe)}

    except Exception as e:
        print("Error creating recipe:", e)
        return {"message": "Recipe creation failed", "error": str(e)}


def get_recipe_service(recipe_id: int = None) -> Union[dict, List[dict]]:
    try:
        if recipe_id:
            response = supabase.from_("recipes").select("*").eq("recipe_id", recipe_id).execute()
            if response.data is not None and response.data:
                return response.data[0]
            else:
                return {"message": "Recipe not found"}
        else:
            response = supabase.from_("recipes").select("*").execute()
            if response.data is not None:
                return response.data
            else:
                return {"message": "No recipes found"}

    except Exception as e:
        print("Error retrieving recipe:", e)
        return {"message": "Error retrieving recipe", "error": str(e)}
    

def get_all_recipe_service( ) -> Union[dict, List[dict]]:
    try:
        response = supabase.from_("recipes").select("*").execute()
        if response.data is not None and response.data:
            return response.data
        else:
            return {"message": "Recipe not found"}

    except Exception as e:
        print("Error retrieving recipe:", e)
        return {"message": "Error retrieving recipe", "error": str(e)}


def update_recipe_service(recipe_id: str, updated_fields: dict) -> dict:
    try:
        if not recipe_exists("recipe_id", recipe_id):
            return {"message": "Recipe does not exist"}

        # Update the recipe
        response = supabase.from_("recipes").update(updated_fields).eq("recipe_id", recipe_id).execute()

        if response.data is not None:
            return {"message": "Recipe updated successfully", "data": response.data}
        else:
            return {"message": "Recipe update failed", "error": response.error}

    except Exception as e:
        print("Error updating recipe:", e)
        return {"message": "Recipe update failed", "error": str(e)}

def delete_recipe_service(recipe_id: str) -> dict:
    try:
        if not recipe_exists("recipe_id", recipe_id):
            return {"message": "Recipe does not exist"}

        # Delete the recipe
        response = supabase.from_("recipes").delete().eq("recipe_id", recipe_id).execute()

        if response.data is not None:
            return {"message": "Recipe deleted successfully"}
        else:
            return {"message": "Recipe deletion failed", "error": response.error}

    except Exception as e:
        print("Error deleting recipe:", e)
        return {"message": "Recipe deletion failed", "error": str(e)}
