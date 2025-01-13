FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
 
COPY . .

RUN pip3 install -r requirements.txt  

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000