import fastapi
from fastapi.params import Depends
from typing import Optional, Any, Coroutine
from typing import List

from models.errors import HTTPError
from models.schemas import ReportBase
from services import openweather_service
from services import report_service

router = fastapi.APIRouter()


@router.get('/api/weather',
            name='weather_info')
async def weather(lat, lon, units: Optional[str] = 'metric'):
    try:
        return await openweather_service.get_report_async(lat, lon, units)
    except HTTPError as err:
        return fastapi.Response(content=err, status_code=err.status_code)


@router.get('/api/reports',
            name='all_reports')
async def reports_get():
    try:
        return await report_service.get_reports_async()
    except HTTPError as err:
        return fastapi.Response(content=err.error_msg, status_code=err.status_code)


@router.post('/api/reports',
             name='add_report')
async def reports_post(report_data: ReportBase):
    try:
        report_dict = report_data.model_dump()
        return await report_service.add_report_async(report_dict)
    except HTTPError as err:
        return fastapi.Response(content=err.error_msg, status_code=err.status_code)


@router.delete('/api/reports/{id}',
               name='delete_report')
async def reports_delete(id: str):
    try:
        return await report_service.delete_report(id)
    except HTTPError as err:
        # err.error_msg = err.error_msg.encode('utf-8')
        return fastapi.Response(content=err.error_msg, status_code=err.status_code)
