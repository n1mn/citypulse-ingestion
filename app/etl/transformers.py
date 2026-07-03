from datetime import datetime, timezone
from app.models.weather import WeatherObservation

"""
    Transforms raw weather API responses into SQLAlchemy models.

    Responsible for mapping external API data into the application's
    internal WeatherObservation model while performing any necessary
    data conversion and normalization.
"""

def json_to_weather_observation(
        weather_json: dict,
        city_id: int,
) -> WeatherObservation:
    """
    Converts a raw OpenWeather API response into a WeatherObservation model.

    Maps the provider's JSON payload to the application's internal
    WeatherObservation entity, preparing it for persistence in the database.
    """
    return WeatherObservation(
        city_id=city_id,
        temperature=weather_json["main"]["temp"],
        humidity=weather_json["main"]["humidity"],
        pressure=weather_json["main"]["pressure"],
        wind_speed=weather_json["wind"]["speed"],
        observed_at=datetime.fromtimestamp(weather_json["dt"], tz=timezone.utc),
    )