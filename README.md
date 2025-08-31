# Weather Coordinates App
A simple Python application that displays weather information based on geographical coordinates and stores it into mokky dev db

# Features

- Get current weather data by coordinates
- Store weather reports in database
- RESTful API endpoints for CRUD operations
- Docker container support
- OpenWeatherMap integration
- Mokky.dev database integration

# Prerequisites

- Python 3.8+
- Docker (optional)
- [OpenWeatherMap API key](https://openweathermap.org/api)
- [Mokky dev API key](https://mokky.dev/projects)

/reports resourse inside mokky.dev db:
```json
[
    {
        "id": 1,
        "description": "cloudy",
        "location": {
            "lat": 51.66,
            "lon": 39.19
        },
        "weeather": {
            "temp": 21.95,
            "units": "metric",
            "name": "Voronezh"
        },
        "created_date": "2025-06-06T22:28:34.635548"
    },
]
```

# Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/anril14/weather_app_mokky.git
cd weather-app
```
2. Edit configuration file
```json
{
  "api_key": "your_openweather_api_key_here",
  "mokky_key": "your_mokky_dev_db_key",
  "mokky_test": "optional_test_key"
}
```
4. Install dependencies
```bash
pip install -r requirements.txt
```
5. Run the application
```bash
uvicorn main:api --host=0.0.0.0 --port=8000 --reload
```
6. Access the application: http://127.0.0.1:8000

# API endpoints (curl)
## GET - Get weather data
```bash
curl --location 'http://127.0.0.1:8000/api/weather?lat=51.66&lon=39.19&units=metric'
```
Query parameters:
* lat (required): Latitude coordinate
* lon (required): Longitude coordinate
* units (optional): Temperature units (metric/imperial)
### Response example:
200 OK
```json
{
    "temp": 29.95,
    "units": "metric",
    "name": "Voronezh"
}
```

## POST - Add weather report to db
```bash
curl --location 'http://127.0.0.1:8000/api/reports' \
--header 'Content-Type: application/json' \
--data '{
    "description": "cloudy",
    "location": {
        "lat": 51.66,
        "lon": 39.19,
        "units": "metric"
    }
}
'
```
### Response example:
200 OK
```json
{
    "description": "cloudy",
    "location": {
        "lat": 51.66,
        "lon": 39.19,
        "units": "metric"
    },
    "weather": {
        "temp": 29.95,
        "units": "metric",
        "name": "Voronezh"
    },
    "created_date": "2025-08-31 13:01:13.620398",
    "id": 1
}
```

## GET - Get all reports
```bash
curl --location 'http://127.0.0.1:8000/api/reports'
```
### Response example:
200 OK
```json
[
    {
        "description": "cloudy",
        "location": {
            "lat": 51.66,
            "lon": 39.19,
            "units": "metric"
        },
        "weather": {
            "temp": 29.95,
            "units": "metric",
            "name": "Voronezh"
        },
        "created_date": "2025-08-31 13:01:13.620398",
        "id": 1
    }
]
```

## DELETE - Delete report from db by id
```bash
curl --location --request DELETE 'http://127.0.0.1:8000/api/reports/1'
```
### Response example:
200 OK
No content

# Docker deployment
```bash
# Build the image
docker build -t weather-app .

# Run the container
docker run -p 8000:8000 weather-app
```
