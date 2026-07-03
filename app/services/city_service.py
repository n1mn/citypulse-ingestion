from sqlalchemy import select
from app.database.session import SessionLocal
from app.models.city import City
from fastapi import APIRouter

class CityService:
    def get_all_cities(self):
        session = SessionLocal()
        try:
            cities = session.scalars(
                select(City)
            ).all()
            return cities
        finally:
            session.close()

