from fastapi.testclient import TestClient
from main import api

client = TestClient(api)

def test_read_root():
    """Проверка GET / на """
    response = client.get('/')
    assert response.status_code == 200
    print(type(response.content))
    print(response.content)

def test_get_weather_correct():
    """Проверка GET /api/weather правильным запросом"""
    pass
def test_get_weather_invalid_types():
    """Проверка GET /api/weather запросом с неправильным типом данных"""
    pass
def test_get_weather_nonexist_required():
    """Проверка GET /api/weather запросом с отсутствием обязательных данных"""
    pass

test_read_root()
