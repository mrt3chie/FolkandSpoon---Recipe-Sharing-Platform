from fastapi import FastAPI, HTTPException
from supabase import create_client, Client
import os
from dotenv import load_dotenv
import logging
from datetime import datetime

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Supabase configuration
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    logger.error("Supabase URL or Key not found in environment variables")
    raise ValueError("Supabase URL or Key not found in environment variables")

logger.info(f"Connecting to Supabase with URL: {SUPABASE_URL}")    
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


# Get Menu Items based on Organization Id
@app.get("/Menu/{org_id}")
def get_digital_menu(org_id: str):
    logger.info(f"Fetching Digital Menu for workspace: {org_id}")
    try:
        response = supabase.table("Menu").select("*").eq("org_id", org_id).execute()
        if not response.data:
            logger.warning(f"Menu Items not found for workspace: {org_id}")
            raise HTTPException(status_code=404, detail="Menu Items not found!")
        logger.info(f"Digital Menu found: {response.data}")
        return response.data
    except Exception as e:
        logger.error(f"Error fetching digital menu: {e}")
        raise HTTPException(status_code=400, detail=str(e))

# Creating Menu Item into Menu Table
@app.post("/Menu/create-menu-item")
def create_menu_item(menu_item: dict):
    logger.info(f"Create Menu Item to the workspace: {menu_item}")
    try:
        response = supabase.table("Menu").insert(menu_item).execute()
        logger.info(f"Menu Item added to the workspace: {response.data}")
        return response.data
    except Exception as e:
        logger.error(f"Error creating Menu Item: {e}")
        raise HTTPException(status_code=400, detail=str(e))

# Updating Menu Item based on Menu Id ( Updating updated_at )
@app.put("/Menu/update-menu-item/{menu_id}")
def update_menu_item(menu_id: str, menu_items: dict):
    
    menu_items['updated_at'] = datetime.now().isoformat()
    logger.info(f"Updating Menu Item to the workspace: {menu_id}")
    try:
        response = supabase.table("Menu").update(menu_items).eq("id",menu_id).execute()
        logger.info(f"Menu Item Updated: {response.data}")
        return response.data
    except Exception as e:
        logger.error(f"Error updating Menu Item: {e}")
        raise HTTPException(status_code=400, detail=str(e))

# Updating Menu Item Status based on Menu Id ( Toggle Switch )    
@app.put("/Menu/update-menu-status/{menu_id}")
def update_menu_status(menu_id: str, IsAvailable: str):
    logger.info(f"Updating Menu Status: {menu_id}")
    try:
        response = supabase.table("Menu").update({"available":IsAvailable}).eq("id",menu_id).execute()
        logger.info(f"Menu Status Updated: {response.data}")
        return response.data
    except Exception as e:
        logger.error(f"Error updating Menu Status: {e}")
        raise HTTPException(status_code=400, detail=str(e))

# Deleting the Menu item from Menu Table using Menu_id
@app.delete("/Menu/delete-menu-item/{menu_id}")
def delete_menu_item(menu_id: str):
    logger.info(f"Deleting Menu Item: {menu_id}")
    try:
        response = supabase.table("Menu").delete().eq("id",menu_id).execute()
        logger.info(f"Menu Item Deleted: {response.data}")
        return "Deleted"
    except Exception as e:
        logger.error(f"Error Deleteing Menu Item: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    

# CRUD operations for category's ( Create, Update)

# Creating new category item in category table
@app.post("/categories/create-category")
def create_category_item(category_item: dict):
    logger.info(f"Create Menu Item to the workspace: {category_item}")
    try:
        response = supabase.table("categories").insert(category_item).execute()
        logger.info(f"category Item added to the workspace: {response.data}")
        return response.data
    except Exception as e:
        logger.error(f"Error creating Category Item {e}")
        raise HTTPException(status_code=400, detail=str(e))

# Updating the Category table based on id
@app.put("/categories/update-category/{category_id}")
def update_menu_status(category_id: str, category_items: dict):
    logger.info(f"Updating category Item: {category_id}")
    try:
        response = supabase.table("categories").update(category_items).eq("id",category_id).execute()
        logger.info(f"category Item Updated: {response.data}")
        return response.data
    except Exception as e:
        logger.error(f"Error updating category item: {e}")
        raise HTTPException(status_code=400, detail=str(e))