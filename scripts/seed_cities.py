from app.database.session import SessionLocal
from app.models.city import City
from sqlalchemy import select
session = SessionLocal()
existing_city = session.scalar(
    select(City). where(
        City.name == "Delhi", 
        City.country_code == "IN" 
        )
)

try:
    if existing_city:
        print(f"City already exists: {existing_city.name} {existing_city.id}")
    else:
        city = City(
            name="Delhi",
            country="India",
            country_code="IN",
            state="Delhi",
            longitude=77.1025,
            latitude=28.7041,
            timezone="Asia/Kolkata",
        )
        session.add(city)
        session.commit()
        session.refresh(city)
        print(f"Seeded city: {city.name} {city.id}") 
finally:
    session.close()