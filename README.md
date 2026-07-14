![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-blue)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.x-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

# 🌦️ CityPulse

A production-style weather data ingestion platform built with FastAPI, PostgreSQL, SQLAlchemy, and Docker.

CityPulse periodically ingests weather data from the OpenWeather API, stores historical observations, and exposes REST APIs for querying cities and weather information.

## 🏗️ Architecture

```mermaid
flowchart TB
    subgraph external["🌐 External Sources"]
        OWM["OpenWeather API"]
        CSV["World Cities CSV<br/>(40k+ cities)"]
    end

    subgraph ingestion["⚙️ Ingestion Tier"]
        SCHED["APScheduler<br/><i>weather_scheduler</i>"]
        subgraph etl["ETL Pipelines"]
            WC["Weather Client<br/>(HTTPX)"]
            TR["Transformers"]
            WP["Weather Pipeline"]
            CIP["City Import Pipeline"]
        end
    end

    subgraph service["🧩 Service Tier"]
        WIS["Weather Ingestion Service"]
        WS["Weather Service"]
        CS["City Service"]
    end

    subgraph data["🗄️ Data Tier"]
        ORM["SQLAlchemy ORM<br/><i>City · WeatherObservation</i>"]
        ALEMBIC["Alembic Migrations"]
        subgraph pg["PostgreSQL (Docker)"]
            CT[("cities")]
            WT[("weather_observations")]
        end
    end

    subgraph api["🚪 API Tier — FastAPI"]
        HEALTH["GET /health"]
        CITIES["GET /cities"]
        LATEST["GET /weather/latest"]
    end

    CLIENT["👤 REST Clients"]

    SCHED -->|"triggers on interval"| WP
    WP --> WC
    OWM -->|"JSON weather data"| WC
    WC --> TR
    TR --> WIS
    CSV --> CIP
    CIP --> CS

    WIS --> ORM
    WS --> ORM
    CS --> ORM
    ORM --> CT
    ORM --> WT
    ALEMBIC -.->|"schema versioning"| pg

    CLIENT --> HEALTH
    CLIENT --> CITIES
    CLIENT --> LATEST
    CITIES --> CS
    LATEST --> WS
```

## ✨ Features

- Import over 40,000 cities from a CSV dataset.
- Fetch real-time weather data using the OpenWeather API.
- Store historical weather observations.
- Automatic scheduled ingestion using APScheduler.
- RESTful APIs built with FastAPI.
- PostgreSQL database managed with SQLAlchemy ORM.
- Alembic database migrations.
- Dockerized development environment.
- Structured logging for ingestion jobs.

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.10 |
| API | FastAPI |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| Database | PostgreSQL |
| Migrations | Alembic |
| Scheduler | APScheduler |
| Containerization | Docker & Docker Compose |
| HTTP Client | HTTPX |
| Weather Provider | OpenWeather API |

## 📁 Project Structure

```text
app/
├── api/
├── clients/
├── core/
├── database/
├── etl/
├── models/
├── scheduler/
├── schemas/
├── services/
└── main.py
```

## 🔄 ETL Workflow

```text
Extract
    │
    ▼
OpenWeather API
    │
    ▼
Weather Client
    │
    ▼
Transformer
    │
    ▼
WeatherObservation Model
    │
    ▼
SQLAlchemy Session
    │
    ▼
PostgreSQL
```

## 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/cities` | List all cities |
| GET | `/weather/latest` | Retrieve the latest weather observations |

## 🚀 Running the Project

```bash
git clone https://github.com/n1mn/citypulse-ingestion.git

cd citypulse-ingestion

uv sync

docker compose up -d

uv run alembic upgrade head

uv run uvicorn app.main:app --reload
```

## 🚀 Future Improvements

- Redis caching
- Kafka-based ingestion pipeline
- Multiple weather providers
- Authentication & Authorization
- Metrics with Prometheus
- Grafana dashboards
- Kubernetes deployment

## 📚 Concepts Demonstrated

- REST API Design
- Layered Architecture
- ETL Pipelines
- Service Layer Pattern
- SQLAlchemy ORM
- Database Relationships
- Transactions
- Batch Processing
- Background Scheduling
- Environment-based Configuration
- Dockerized Development
- Structured Logging

## 📌 Project Status

✅ Version: **v1.0**

This project demonstrates a production-style backend architecture for weather data ingestion using FastAPI, PostgreSQL, SQLAlchemy, Docker, and APScheduler.

Future versions will introduce Kafka, Redis, distributed processing, and cloud deployment.

## 👨‍💻 Author

**Naman Sharma**

Built as part of a Data Engineering portfolio focused on production-grade backend systems and modern data platforms.