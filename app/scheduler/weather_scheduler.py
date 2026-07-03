from apscheduler.schedulers.background import BackgroundScheduler

from app.core.logging import logger
from app.services.weather_ingestion_service import WeatherIngestionService  

scheduler = BackgroundScheduler()

scheduler.add_job(
    WeatherIngestionService().run,
    trigger="interval",
    hours=1,
    id="weather_ingestion_job",
)
def start_scheduler():
    logger.info("Starting the weather ingestion scheduler.")
    scheduler.start()