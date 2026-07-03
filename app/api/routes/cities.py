from fastapi import APIRouter

from app.schemas.city import CityResponse
from app.services.city_service import CityService

router = APIRouter()

@router.get("/cities", response_model=list[CityResponse])
def get_all_cities():
    service = CityService()
    cities = service.get_all_cities()
    return cities