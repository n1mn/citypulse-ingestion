"""
HTTP client for interacting with the OpenWeather API.

Provides a reusable interface for retrieving weather data
from external services.
"""
import httpx

from app.core.config import settings


class WeatherClient:

    """
    Client responsible for communicating with the OpenWeather API.

    Handles authenticated HTTP requests, retrieves current weather
    information for a given geographic location, and returns the
    raw API response for further processing.
    """
     
    def __init__(self)-> None:
        self.base_url = settings.weather_base_url
        self.api_key = settings.weather_api_key
        self.timeout = settings.weather_timeout

        self.client = httpx.Client(
            base_url=self.base_url,
            timeout=self.timeout,
        )
    def get_current_weather(
            self,
            latitude: float,
            longitude: float,
    ) -> dict:
        response = self.client.get(
            "/weather",
            params={
                "lat": latitude,
                "lon": longitude,
                "appid": self.api_key,
                "units": "metric",
            },
        )
        response.raise_for_status()
        return response.json()
        

