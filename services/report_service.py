import datetime
import uuid
from typing import List
from typing import Optional

from models.errors import HTTPError
from .openweather_service import api_key
from .openweather_service import validate_units
import httpx

mokky_key: Optional[str] = None


async def get_reports_async():
    url = f'https://{mokky_key}.mokky.dev/reports'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPError(response.text, response.status_code)
        return response.json()


async def add_report_async(report_data: dict):
    report_data = validate_report_data(report_data)

    url = f'https://api.openweathermap.org/data/2.5/weather?lat={report_data["location"]["lat"]}&lon={report_data["location"]["lon"]}&appid={api_key}&units={report_data["location"]["units"]}'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPError(response.text, response.status_code)
    data = response.json()
    report_data['weather'] = {'temp': data['main']['temp'],
                              "units": report_data['location']['units'],
                              "name": data['name']}

    now = datetime.datetime.now()
    report_data["created_date"] = str(now)

    url = f'https://{mokky_key}.mokky.dev/reports'
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=report_data)
        if response.status_code != 201:
            raise HTTPError(response.text, response.status_code)
        return response.json()


async def delete_report(id: str):
    url = f'https://{mokky_key}.mokky.dev/reports/{id}'
    async with httpx.AsyncClient() as client:
        response = await client.delete(url)
        if response.status_code != 204:
            raise HTTPError(response.text, response.status_code)
        return response.json()


def validate_report_data(report_data) -> dict:
    if set(report_data.keys()) != {'description', 'location'}:
        error = f'Invalid input json keys'
        raise HTTPError(status_code=422, error_msg=error)

    if set(report_data.get("location").keys()) != {'lon', 'lat', 'units'}:
        if set(report_data.get("location").keys()) != {'lon', 'lat'}:
            error = f'Invalid input json keys inside "location"'
            raise HTTPError(status_code=422, error_msg=error)
        report_data["location"]["units"] = "metric"

    (report_data["location"]["lat"],
     report_data["location"]["lon"],
     report_data["location"]["units"]) = \
        validate_units(lat=report_data["location"]["lat"],
                       lon=report_data["location"]["lon"],
                       units=report_data["location"]["units"],
                       error_code=422)

    return report_data
