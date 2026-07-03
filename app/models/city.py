from datetime import datetime
from sqlalchemy import DateTime, Float, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

class City(Base):
    __tablename__ = "cities"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(100), nullable=False)

    country: Mapped[str] = mapped_column(String(100), nullable=False)

    country_code: Mapped[str] = mapped_column(String(2), nullable=False)

    state: Mapped[str | None] = mapped_column(String(100))

    longitude: Mapped[float] = mapped_column(Float, nullable=False)

    latitude: Mapped[float] = mapped_column(Float, nullable=False)

    timezone: Mapped[str] = mapped_column(String(100), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
     
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    weather_observations = relationship(
        "WeatherObservation",
        back_populates="city",
     )