import fastapi
import uvicorn
import json

from pathlib import Path
from views import home
from api import weather_api
from services import openweather_service
from services import report_service

api = fastapi.FastAPI()


def configure():
    configure_routing()
    configure_api_keys()


def configure_api_keys():
    file = Path('settings.json').absolute()
    if not file.is_file:
        raise Exception("settings.json not found")

    with open('settings.json') as f:
        settings = json.load(f)
        openweather_service.api_key = settings.get('api_key')
        report_service.api_key = settings.get('api_key')
        report_service.mokky_key = settings.get('mokky_key')


def configure_routing():
    api.include_router(weather_api.router)
    api.include_router(home.router)


if __name__ == '__main__':
    configure()
    uvicorn.run(api, host='127.0.0.1', port=8000)
else:
    configure()
