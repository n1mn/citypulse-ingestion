from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.database import session
from app.database.session import SessionLocal
from app.models.weather import WeatherObservation


class WeatherService:
    """
    Handles retrieval of weather observations from the database.

    Provides business logic for querying weather data while remaining
    independent of the API layer and HTTP-specific concerns.
    """

    def get_latest_weather(self):
        session = SessionLocal()
        try:
            observations = session.scalars(
                select(WeatherObservation)
                .options(joinedload(WeatherObservation.city))
                .order_by(WeatherObservation.observed_at.desc())
            ).all()
            return observations
        finally:
            session.close()
