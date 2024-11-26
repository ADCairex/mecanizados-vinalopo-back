from fastapi import APIRouter
from .search_ot import router as search_ot_router

api_router = APIRouter()
api_router.include_router(search_ot_router, prefix="/search-ot")
