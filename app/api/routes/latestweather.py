from fastapi import APIRouter

from app.services.weather_service import WeatherService
from app.schemas.weather import WeatherResponse

router = APIRouter(
    prefix="/weather",
    tags=["Weather"],
)

@router.get(
    "/latest",
    response_model=list[WeatherResponse],
)
def latest_weather():
    service = WeatherService()
    observations = service.get_latest_weather()
    
    return [
        WeatherResponse(
            city=observation.city.name,
            temperature=observation.temperature,
            humidity=observation.humidity,
            pressure=observation.pressure,
            wind_speed=observation.wind_speed,
            observed_at=observation.observed_at,
        )
          for observation in observations
    ]
    