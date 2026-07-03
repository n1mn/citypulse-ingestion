from datetime import datetime

from pydantic import BaseModel, ConfigDict

class WeatherResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    city: str
    temperature: float
    humidity: float
    pressure: float
    wind_speed: float
    observed_at: datetime