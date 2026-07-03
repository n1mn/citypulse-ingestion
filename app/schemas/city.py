from pydantic import BaseModel, ConfigDict

class CityResponse(BaseModel):
    id: int
    name: str
    country: str
    country_code: str
    state: str
    latitude: float
    longitude: float
    timezone: str

    model_config = ConfigDict(from_attributes=True)