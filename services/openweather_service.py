from typing import Optional, Tuple

import httpx

from models.errors import HTTPError

api_key: Optional[str] = None

async def get_report_async(lat: str, lon: str, units: Optional[str] = 'metric') -> dict:
    lat, lon, units = validate_units(lat, lon, units)
    print(units)
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units={units}'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPError(response.text, response.status_code)

    data = response.json()
    return {'temp': data['main']['temp'], "units": units, "name": data['name']}


def validate_units(lat: str, lon: str, units: Optional[str], error_code: Optional[int]=400) -> \
        Tuple[float, float, Optional[str]]:
    try:
        lat = float(lat)
        lon = float(lon)
    except (TypeError, ValueError):
        error = f'Invalid type for latitude or longitude - must be numeric'
        raise HTTPError(status_code=error_code, error_msg=error)

    if not (-90 <= lat <= 90):
        error = f'Invalid latitude {lat} - must be between -90 and 90'
        raise HTTPError(status_code=error_code, error_msg=error)
    if not (-180 <= lon <= 180):
        error = f'Invalid longitude {lon} - must be between -180 and 180'
        raise HTTPError(status_code=error_code, error_msg=error)

    valid_units = {'standard', 'metric', 'imperial'}
    if units not in valid_units:
        error = f'invalid units {units}, it must be one of {valid_units}'
        raise HTTPError(status_code=error_code, error_msg=error)
    return lat, lon, units
