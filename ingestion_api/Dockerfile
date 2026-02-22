FROM python:3.11-slim
WORKDIR /app
COPY ingestion_api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY shared /app/shared
COPY ingestion_api /app/ingestion_api
EXPOSE 8000
CMD ["uvicorn", "ingestion_api.main:app", "--host", "0.0.0.0", "--port", "8000"]


