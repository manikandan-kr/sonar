FROM python:3.11-slim

WORKDIR /app

COPY . .
# RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -e .[dev]

EXPOSE 8000

CMD ["uvicorn", "analytics_mcp.server:app", "--host", "0.0.0.0", "--port", "8000"]
