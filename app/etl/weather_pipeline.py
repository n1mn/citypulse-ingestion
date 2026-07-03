"""
Weather ingestion pipeline.

Implements the Extract–Transform–Load (ETL) workflow for
retrieving weather data from external providers and storing
it in the database.
"""
from sqlalchemy.orm import Session

from app.clients.weather_client import WeatherClient
from app.etl.transformers import json_to_weather_observation
from app.models.city import City

def ingest_weather_for_city(
  city:City,
  session: Session,
  client: WeatherClient,
) -> None:
  
  """
    Retrieves and stores the latest weather observation for a city.

    Executes the Extract–Transform–Load (ETL) workflow by fetching
    weather data from the external API, transforming it into the
    application's data model, and staging it for persistence.
  """

  weather_json = client.get_current_weather(
    latitude = city.latitude,
    longitude = city.longitude,
  )
  observation = json_to_weather_observation(
    weather_json=weather_json,
    city_id = city.id,
  )
  
  session.add(observation)
  

 