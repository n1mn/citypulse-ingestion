from datetime import datetime
from sqlalchemy import DateTime, Float, String, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

class WeatherObservation(Base):
    __tablename__ = "weather_observations"

    id: Mapped[int] = mapped_column(primary_key = True)

    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"), nullable = False)

    temperature : Mapped[float] = mapped_column(Float, nullable = False)

    humidity: Mapped[float] = mapped_column(Float, nullable = False)

    pressure: Mapped[float] = mapped_column(Float, nullable = False)

    wind_speed: Mapped[float] = mapped_column(Float, nullable = False)

    observed_at: Mapped[datetime] = mapped_column(
        DateTime (timezone = True),
        nullable = False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone = True),
        server_default = func.now(),
        nullable = False,
    )
    city = relationship("City", back_populates="weather_observations")
