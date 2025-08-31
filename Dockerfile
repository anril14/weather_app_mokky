FROM python:3.12

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD uvicorn main:api --host=0.0.0.0