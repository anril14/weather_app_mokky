# Weather Coordinates App
A simple Python application that displays weather information based on geographical coordinates and stores it into mokky dev db.
Hosting on 127.0.0.1:8000

### Prerequisites

- Python 3.8+
- Docker (optional)
- [OpenWeatherMap API key](https://openweathermap.org/api)
- [Mokky dev API key](https://mokky.dev/projects)

/reports resourse:
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

Requires settings.json file in root folder with format:
{
  "api_key": "your_openweather_api_key_here",
  "mokky_key": "your_mokky_dev_db_key",
  "mokky_test": "optional_test_key"
}
