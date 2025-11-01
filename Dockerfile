# syntax=docker/dockerfile:1
 
FROM python:3.12-slim
 
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
 
WORKDIR /app
 
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
 
COPY . /app/
 
EXPOSE 8000
 
ENV AWS_REGION=us-east-2
 
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:create_app()"]