from sqlalchemy import select
from app.core.logging import logger
from app.clients.weather_client import WeatherClient
from app.database.session import SessionLocal
from app.etl.weather_pipeline import ingest_weather_for_city
from app.models.city import City
from app.services.weather_ingestion_service import WeatherIngestionService

def main():
    service = WeatherIngestionService()
    service.run()

if __name__ == "__main__":
        main()