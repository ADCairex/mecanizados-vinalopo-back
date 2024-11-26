from fastapi import APIRouter
from src.models.search_ot import OTDetail, OTTime, OTPurchase
from src.services.search_ot import SearchOTService
from src.repositories.search_ot import SearchOTRepository

repository = SearchOTRepository()
search_ot_service = SearchOTService(repository)

router = APIRouter()

@router.get("/detail/{ot_id}", tags=["search-ot"])
def get_ot_details(ot_id: int) -> OTDetail:
    """Endpoint to obtain the details of the OT."""
    return search_ot_service.get_details(ot_id)

@router.get("/times/{ot_id}", tags=["search-ot"])
def get_ot_times(ot_id: int) -> list[OTTime]:
    """Endpoint to obtain the times of the OT."""
    return search_ot_service.get_times(ot_id)

@router.get("/purchases/{ot_id}", tags=["search-ot"])
def get_ot_purchases(ot_id: int) -> list[OTPurchase]:
    """Endpoint to obtain the purchases of the OT."""
    return search_ot_service.get_purchases(ot_id)
