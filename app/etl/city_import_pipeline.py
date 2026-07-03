import csv

from sqlalchemy import select

from app.core.logging import logger
from app.database.session import SessionLocal
from app.models.city import City

BATCH_SIZE = 1000


def import_cities(csv_path: str) -> None:
    """
    Imports city records from a CSV dataset into the database.

    Performs validation, duplicate detection using geographic
    coordinates, and batch insertion for efficient loading.
    """
    session = SessionLocal()

    imported = 0
    duplicates = 0
    invalid = 0

    existing_locations = {
        (lat, lng)
        for lat, lng in session.execute(
            select(City.latitude, City.longitude)
        )
    }
      

    cities_to_insert = []

    try:
        with open(csv_path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:

                # Validate required fields
                if (
                    not row["city"]
                    or not row["country"]
                    or not row["iso2"]
                    or not row["lat"]
                    or not row["lng"]
                ):
                    invalid += 1
                    continue

                lat = float(row["lat"])
                lng = float(row["lng"])

                # Skip duplicates
                if (lat, lng) in existing_locations:
                    duplicates += 1
                    continue

                city = City(
                    name=row["city"],
                    country=row["country"],
                    country_code=row["iso2"],
                    state=row["admin_name"],
                    latitude=lat,
                    longitude=lng,
                    timezone=row.get("timezone", "UTC"),
                )

                cities_to_insert.append(city)

                # Prevent duplicates within the same CSV import
                existing_locations.add((lat, lng))

                imported += 1

                # Batch insert
                if len(cities_to_insert) >= BATCH_SIZE:
                    session.add_all(cities_to_insert)
                    session.commit()
                    cities_to_insert.clear()

        # Insert remaining cities
        if cities_to_insert:
            session.add_all(cities_to_insert)
            session.commit()

        logger.info("=" * 40)
        logger.info("City Import Summary")
        logger.info("=" * 40)
        logger.info(f"Imported      : {imported}")
        logger.info(f"Duplicates    : {duplicates}")
        logger.info(f"Invalid Rows  : {invalid}")
        logger.info("=" * 40)

    except Exception:
        session.rollback()
        logger.exception("City import failed.")
        raise

    finally:
        session.close()