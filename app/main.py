from fastapi import FastAPI
from app.core.config import settings
from app.api.routes.health import router as health_router
from app.api.routes.cities import router as cities_router
from app.api.routes.weather import router as weather_router
from app.api.routes.latestweather import router as latest_weather_router

from contextlib import asynccontextmanager
from app.scheduler.weather_scheduler import scheduler

@asynccontextmanager
async def lifespan(app: FastAPI):
    if settings.enable_scheduler:
        scheduler.start()
    yield
    scheduler.shutdown()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    lifespan=lifespan
)
app.include_router(health_router)
app.include_router(cities_router)
app.include_router(weather_router)
app.include_router(latest_weather_router)

@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.app_name}"
    }


