from fastapi import APIRouter
from app.services.weather_ingestion_service import WeatherIngestionService

router = APIRouter()

@router.post("/weather/ingest")
def ingest_weather():
    service = WeatherIngestionService()
    service.run()
    return {"message": "Weather ingestion completed."}