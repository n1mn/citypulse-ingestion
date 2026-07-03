import time
from sqlalchemy import select
from app.core.logging import logger
from app.clients.weather_client import WeatherClient
from app.database.session import SessionLocal
from app.etl.weather_pipeline import ingest_weather_for_city
from app.models.city import City
from app.core.config import settings

class WeatherIngestionService:
    """
    Coordinates the weather ingestion workflow.

    Retrieves cities from the database, fetches their latest weather
    from the external provider, and persists weather observations
    while handling logging, transactions, and failures.
    """
    def run(self):
        session = SessionLocal()
        client = WeatherClient()

        try:
            cities = session.scalars(
                select(City)
                .limit(settings.weather_ingestion_limit)
            ).all()
            logger.info(f"Starting weather ingestion for {len(cities)} cities.")

            for city in cities:
                try:
                    logger.info(f"Processing {city.name} {city.id}")
                    ingest_weather_for_city(
                        city=city,
                        session=session,
                        client=client
                    )
                    session.commit()
                    time.sleep(1)
                    logger.info(f"Successfully ingested weather for {city.name}")
                except Exception as e:
                    logger.error(f"Failed to ingest weather for {city.name}: {e}")
                    session.rollback()
            
        finally:
            session.close()
            
        logger.info("Weather ingestion completed.")
