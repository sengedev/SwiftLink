FROM python:3.12.4-alpine3.20

WORKDIR /app/swiftlink

COPY server/ ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
