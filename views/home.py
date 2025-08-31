import fastapi
from fastapi.responses import HTMLResponse

router = fastapi.APIRouter()


@router.get('/', include_in_schema=False)
def index():
    body = ('''
        <html>
            <head>
                <title>Scherbakov weather API</title>
            </head>
            <body>
                <h1>Scherbakov weather API</h1>
                <div>
                    <a>GET</a><br>
                    <a href='/api/weather?lat=51.66&lon=39.19'>/api/weather?lat=51.66&lon=39.19</a><br>
                    <a href='/api/weather/?lat=51.66&lon=abc'>/api/weather/?lat=51.66&lon=abc</a><br>
                    <a href='/api/weather/?lat=51.66&lon=39.19&units=blablalba'>/api/weather/?lat=51.66&lon=39.19&units=blablalba</a><br>
                    <a>Other requests (DELETE, POST) in postman</a><br>
                </div>
            </body>
        </html>
        ''')
    return HTMLResponse(content=body)
